def get_supported_tls(version):
    return ["TLS10", "TLS11", "TLS12"]


def extract_versions(tags):
    # Only keep the tags that mark a release. These start with 'mbedtls' or
    # 'polarssl'.
    tags = [tag for tag in tags if tag.startswith("mbedtls") or tag.startswith("polarssl")]

    # Do not include any pre-releases, as those often don't work properly.
    tags = [tag for tag in tags if "alpha" not in tag and "pre" not in tag and "rc" not in tag and "preview" not in tag]

    # Extract version numbers
    version_info = [{
        "tag": tag,
        "version": tag.replace("polarssl-", "").replace("mbedtls-", ""),
    } for tag in tags]

    # Filter out versions pre 1.0, these do not provide a 'make install'
    # target.
    version_info = [info for info in version_info if info["version"]  >= "1.0"]

    # Add info about supported TLS versions
    for info in version_info:
        info["supported_tls"] = get_supported_tls(info["version"])

    return version_info
