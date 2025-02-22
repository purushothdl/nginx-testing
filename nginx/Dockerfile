FROM openresty/openresty:alpine

# Install dependencies
RUN apk add --no-cache \
    git \
    gcc \
    musl-dev \
    lua5.1-dev \
    luarocks5.1 \
    openssl-dev

# Install Lua JWT modules
RUN luarocks-5.1 install lua-resty-openssl && \
    luarocks-5.1 install lua-resty-jwt

# Remove all default configurations
RUN rm -rf /etc/nginx/conf.d/* && \
    rm -rf /usr/local/openresty/nginx/html/*

# Create necessary directories
RUN mkdir -p /usr/local/openresty/nginx/conf && \
    mkdir -p /etc/nginx/lua

# Copy configurations
COPY nginx.conf /usr/local/openresty/nginx/conf/nginx.conf
COPY conf.d/ /etc/nginx/conf.d/
COPY lua/ /etc/nginx/lua/

# Expose port
EXPOSE 80

# Start NGINX
CMD ["/usr/local/openresty/bin/openresty", "-g", "daemon off;"]