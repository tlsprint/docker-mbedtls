# This file is automatically generated with Dockerfile.j2 as a template. Do not
# edit by hand, since your changes will be lost!
FROM buildpack-deps AS builder

# Create a shallow clone of the implementation repository in the work directory,
# containing only the code of the specified version/tag.
WORKDIR /mbedtls
RUN git clone --branch polarssl-1.2.10 --depth 1 https://github.com/ARMmbed/mbedtls.git .

# Version 1.2.10 and earlier do not have a properly working ssl_server.c file.
# By copying a more recent version (from 1.2.11), this is mitigated.
RUN wget -O programs/ssl/ssl_server.c https://raw.githubusercontent.com/ARMmbed/mbedtls/polarssl-1.2.11/programs/ssl/ssl_server.c
RUN wget -O programs/ssl/ssl_server2.c https://raw.githubusercontent.com/ARMmbed/mbedtls/polarssl-1.2.11/programs/ssl/ssl_server2.c

# Install build depencency cmake
RUN apt-get update && apt-get install -y cmake

# Build
RUN cmake -D CMAKE_BUILD_TYPE:String="Release" .
RUN make

# Install to a temporary directory
RUN make install DESTDIR=/tmp/package-dir

# Install package to a new container, so we can be sure that we are running
# this specific package.
FROM debian
COPY --from=builder /tmp/package-dir /
RUN ldconfig

# Expose the default port
EXPOSE 4433

# Start the server
CMD ssl_server