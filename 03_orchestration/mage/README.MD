
## Orchestration - Mage

### <ins>Introduction</ins>
Mage is orchestrator tool, it is an open-source pipeline tools for orchestrating, transforming and integrating data.

### <ins>Mage in Codespaces</ins>
1. Forked from [`mage-ai/mlops`](https://github.com/mage-ai/mlops).
2. Find `Create codespace on master` and click it.
3. Docker container is available in codespaces. In the command prompt, run the following command.
```bash
    ./scripts/start.sh
```
4. Once the Docker container finishes starting up, navigate to `PORTS` in codespaces to obtain url with port `6789` then run it in web browser.
5. Alternatively, you can run it in your local VS Code by execute `Open in VS Code Desktop`.
6. To use `mage start mlops`, install this.
```bash
pip install botocore mage-ai
```

### <ins>Window with docker-compose</ins>
1. Clone the respository
```bash
git clone https://github.com/mage-ai/mlops.git
cd mlops
```
2. Code modification

`start.sh`
```bash
export PROJECT_NAME=mlops
export MAGE_CODE_PATH=home/src
export SMTP_EMAIL=$SMTP_EMAIL
export SMTP_PASSWORD=$SMTP_PASSWORD
docker-compose up
```

`docker-compose.yml`
```bash
volumes:
    # Mount your local codebase to the container.
    - "${PWD}:/${MAGE_CODE_PATH}"
    # Store the data output on local machine to easily debug (optional).
    - "~/.mage_data:/${MAGE_CODE_PATH}/mage_data"
    # Initial credentials to create an IAM user with limited permissions for deployment.
    - "~/.aws:/root/.aws"
    # Local machine’s SSH keys to pull and push to your GitHub repository.
    - "~/.ssh:/root/.ssh:ro"
    # Local machine’s GitHub configs
```

3. Launch Mage and database service (PostgreSQL)
```bash
./scripts/start.sh
```

4. Open [`http://localhost:6789`](http://localhost:6789) in browser.

### <ins>Issue</ins>
1. Codespaces
<br>Docker auto-creates `.gitconfig` as a directory instead of a file.
```bash
warning: unable to access '/home/codespace/.gitconfig': Is a directory
warning: unable to access '/home/codespace/.gitconfig': Is a directory
```
