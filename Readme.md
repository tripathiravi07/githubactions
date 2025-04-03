# GitHub Actions Deployment with Kubernetes

This repository demonstrates how to set up a **GitHub Actions** workflow to build a Docker image, push it to **Docker Hub**, and deploy it to a **Kubernetes cluster**.

## Prerequisites

Before you begin, ensure you have the following:

- **Docker Hub Account**: To store and retrieve your Docker images.
- **Kubernetes Cluster**: A running Kubernetes cluster accessible from the GitHub Actions runner.
- **GitHub Secrets**: The following secrets should be configured in your repository:
  - `DOCKERHUB_USERNAME`: Your Docker Hub username.
  - `DOCKERHUB_PASSWORD`: Your Docker Hub password or access token.
  - `KUBECONFIG_DATA`: Base64-encoded Kubeconfig file for accessing your Kubernetes cluster.

## Repository Structure

```
.
├── .github
│   └── workflows
│       └── myfirstwf.yaml # GitHub Actions workflow
├── api.yaml
├── ecs-api.py
├── requirements.txt     # Python dependencies
├── Dockerfile           # Dockerfile for building the application image
└── README.md            # Project documentation
```

## GitHub Actions Workflow

The [myfirstwf.yaml](.github/workflows/myfirstwf.yaml) workflow automates the following steps:

1. **Checkout Repository**: Retrieves the latest code from the repository.
2. **Log in to Docker Hub**: Authenticates to Docker Hub using the provided secrets.
3. **Build and Push Docker Image**: Builds the Docker image from the `Dockerfile` and pushes it to Docker Hub.
4. **Apply Kubernetes Manifests**: Deploys the updated manifests to the Kubernetes cluster.

## Setting Up the Environment

1. **Configure GitHub Secrets**:
   - Navigate to your repository's **Settings** > **Secrets and variables** > **Actions**.
   - Add the following secrets:
     - `DOCKERHUB_USERNAME`: Your Docker Hub username.
     - `DOCKERHUB_PASSWORD`: Your Docker Hub password or access token.

2. **Prepare Kubernetes Manifests**:
   - Ensure the `api.yaml` files are correctly configured for your application.

3. **Trigger the Workflow**:
   - Push changes to the `main` branch to trigger the GitHub Actions workflow.

## Notes

- Ensure your Kubernetes cluster is accessible from the GitHub Actions runner.
- The `KUBECONFIG_DATA` secret should contain the base64-encoded content of your Kubeconfig file. You can generate it using:

  ```bash
  cat $HOME/.kube/config | base64
  ```

  Then, add the output as the `KUBECONFIG_DATA` secret.

- The `deploy.yml` workflow is set to run on pushes to the `main` branch. Modify the `on` section of the workflow file to suit your needs.

---

This `README.md` provides a comprehensive overview of your project's purpose, structure, and setup instructions. Ensure to replace placeholders with your actual information where necessary.

