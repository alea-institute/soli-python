from soli import SOLI

if __name__ == "__main__":
    # Initialize the SOLI client with default settings
    soli = SOLI()
    print(soli)

    # Initialize with custom settings
    soli_custom = SOLI(
        source_type="github",
        github_repo_owner="alea-institute",
        github_repo_name="SOLI",
        github_repo_branch="main",
        use_cache=True,
    )
    print(soli_custom)

    # Initialize from a custom HTTP URL
    soli_http = SOLI(
        source_type="http",
        http_url="https://github.com/alea-institute/SOLI/raw/main/SOLI.owl",
    )
    print(soli_http)
