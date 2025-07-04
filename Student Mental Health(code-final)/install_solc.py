from solcx import install_solc, get_installed_solc_versions

solc_version = '0.8.0'
if solc_version not in get_installed_solc_versions():
    install_solc(solc_version)
else:
    print(f'Solc {solc_version} is already installed.')
