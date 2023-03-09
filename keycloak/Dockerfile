FROM alpine:latest as theme-installer
# we have to use alpine here because the keycloak image is extremely stripped down

# Argument to select git ref
ARG KEYCLOAK_THEME_GIT_REF
ENV KEYCLOAK_THEME_GIT_REF=${KEYCLOAK_THEME_GIT_REF:-main}
ENV KEYCLOAK_THEME_TARBALL_URL=https://github.com/mitodl/odl-custom-keycloak/archive/${KEYCLOAK_THEME_GIT_REF}.tar.gz

RUN apk add git
RUN cd /tmp && wget $KEYCLOAK_THEME_TARBALL_URL -O - | tar -C /tmp -xzf - --strip-components=1

FROM quay.io/keycloak/keycloak:latest as builder
COPY --from=theme-installer /tmp/themes/ /opt/keycloak/themes/

WORKDIR /opt/keycloak
RUN /opt/keycloak/bin/kc.sh build


# -------------------------------------------------------------------------
FROM quay.io/keycloak/keycloak:latest
COPY --from=builder /opt/keycloak /opt/keycloak

ENTRYPOINT ["/opt/keycloak/bin/kc.sh"]