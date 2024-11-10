# 📬 Mail Server Project with Ubuntu and Roundcube

This project sets up a mail server with a webmail interface using Roundcube, along with additional tooling for automation, provisioning, and deployment. It leverages Docker, Vagrant, and Python for a smooth deployment experience on Ubuntu.

## 🗂️ Table of Contents

- [📬 Mail Server Project with Ubuntu and Roundcube](#-mail-server-project-with-ubuntu-and-roundcube)
  - [🗂️ Table of Contents](#️-table-of-contents)
  - [📖 Project Description](#-project-description)
    - [🛑 Considerations](#-considerations)
    - [📂 Project Structure](#-project-structure)
  - [✅ Requirements](#-requirements)
  - [🔧 Installation and Setup](#-installation-and-setup)
  - [🚀 Running the Project](#-running-the-project)
  - [📧 Accessing Roundcube Webmail](#-accessing-roundcube-webmail)
  - [⚙️ CI/CD and Deployment](#️-cicd-and-deployment)
    - [CI Pipeline](#ci-pipeline)
    - [🌐 Deployment on Render](#-deployment-on-render)
  - [🛠️ Technologies Used](#️-technologies-used)
  - [🏗️ Architecture](#️-architecture)
  - [🤝 Contributing](#-contributing)
  - [📜 License](#-license)

## 📖 Project Description

This project configures a basic mail server on an Ubuntu environment using Postfix, Dovecot, and Roundcube as the webmail client. It also incorporates Docker and Vagrant for deployment automation and Python for scripting additional setup steps.

### 🛑 Considerations

- **Security**: Basic security measures are in place, but additional configurations are recommended for production, such as SSL for email encryption and advanced user authentication.

### 📂 Project Structure

```plaintext
.
├── .github
│   ├── dependabot.yml
│   └── workflows
│       ├── ci-pipeline.yml
│       └── cd-pipeline.yml
├── config/
│   ├── postfix/
│   ├── dovecot/
│   └── roundcube/
├── scripts/
│   ├── setup_mail.sh
│   └── setup_roundcube.py
├── docker-compose.yml
├── Vagrantfile
└── README.md

```

# 📬 Mail Server Project with Ubuntu and Roundcube

Este proyecto configura un servidor de correo con interfaz web mediante Roundcube, usando Docker, Vagrant y Python en un entorno Ubuntu.

## ✅ Requirements

- 🐍 **[Python](https://www.python.org/downloads/)** (versión 3.6 o superior): Para scripting y configuración.
- 🐳 **[Docker](https://www.docker.com/get-started)**: Para la contenedorización de aplicaciones.
- 🛠️ **[Docker Compose](https://docs.docker.com/compose/install/)**: Para administrar aplicaciones multi-contenedor.
- 📦 **[Vagrant](https://www.vagrantup.com/downloads)**: Para la provisión de máquinas virtuales.
- 🌐 **[Git](https://git-scm.com/downloads)**: Para control de versiones.
- 🐧 **[Ubuntu Server](https://ubuntu.com/download/server)** (por ejemplo, Ubuntu 20.04 o posterior): Sistema operativo del servidor.
- 🚀 **[GitHub Actions](https://github.com/features/actions)**: Para CI/CD workflows.
- 🌐 **[Render](https://render.com/)**: Para despliegue y gestión de la aplicación.

---

## 🔧 Installation and Setup

1. **Clone the Repository**:

   ```bash
   git clone https://github.com/your-username/mail-server-project.git
   cd mail-server-project/

   ```

## 🚀 Running the Project

This launches the full stack, including Roundcube, configured as a webmail client for the mail server.

## 📧 Accessing Roundcube Webmail

Once the setup completes, you can access the Roundcube webmail interface by navigating to [http://localhost](http://localhost) in your browser.

## ⚙️ CI/CD and Deployment

The project uses **GitHub Actions** for continuous integration (CI) and **Render** for continuous deployment (CD).

### CI Pipeline

Each push to the `main` branch triggers the following CI pipeline steps:

1. **Unit Testing**: Executes tests to ensure code integrity.
2. **Build**: Builds Docker images for the mail server and Roundcube.
3. **Deployment**: Deploys to **Render** if all steps pass successfully.

### 🌐 Deployment on Render

The project is configured to deploy on **Render**, which provides a managed server environment for easy deployment and scaling.

- **Webmail Interface**: The Roundcube webmail client can be accessed at [https://mail-project.render.com](https://mail-project.render.com) after deployment.

## 🛠️ Technologies Used

- **Email Server**: Postfix, Dovecot.
- **Webmail Client**: Roundcube.
- **Automation and Provisioning**: Vagrant, Docker, Docker Compose.
- **CI/CD**: GitHub Actions, Render.
- **Scripting**: Bash, Python.
- **Development**: Git, Ubuntu Server.

## 🏗️ Architecture

For detailed information on the system's architecture, refer to the [Architecture Guide](./docs/guides/ARCHITECTURE.md).

## 🤝 Contributing

To contribute to this project, please check out our [Contribution Guide](./docs/guides/CONTRIBUTING.md) for instructions on setting up your development environment and the process for submitting contributions.

## 📜 License

This project is licensed under the MIT License.
