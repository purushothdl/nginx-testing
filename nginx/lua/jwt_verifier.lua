local jwt = require "resty.jwt"

-- Get the secret key from environment variable
local secret_key = os.getenv("SECRET_KEY")
if not secret_key then
    ngx.log(ngx.ERR, "Missing SECRET_KEY environment variable")
    ngx.exit(500)
end

local auth_header = ngx.var.http_authorization
if not auth_header then
    ngx.log(ngx.ERR, "Missing Authorization header")
    ngx.exit(401)
end

local token = auth_header:match("Bearer%s+(.+)")
if not token then
    ngx.log(ngx.ERR, "Invalid Authorization header format")
    ngx.exit(401)
end

-- Simple verification without complex validation
local jwt_obj = jwt:verify(secret_key, token)

if not jwt_obj.verified then
    ngx.log(ngx.ERR, "Invalid JWT: " .. jwt_obj.reason)
    ngx.exit(401)
end

if not jwt_obj.payload.sub then
    ngx.log(ngx.ERR, "Missing sub claim in JWT")
    ngx.exit(401)
end

-- Set the user id from the verified token
ngx.var.user_id = jwt_obj.payload.sub

-- Log successful verification
ngx.log(ngx.INFO, "JWT verified successfully for user: " .. jwt_obj.payload.sub)