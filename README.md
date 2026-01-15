# Azure Flask Article CMS

This project is a simple Content Management System (CMS) built using the Flask framework and deployed using Microsoft Azure services. The application allows users to log in, create articles, and upload images for each article.

---

## Features

- User authentication using username and password
- Create and view articles
- Upload article images
- Data persistence using Azure SQL Database
- Image storage using Azure Blob Storage

---

## Azure Services Used

- **Azure SQL Database** – Stores users and article data
- **Azure Blob Storage** – Stores uploaded article images
- **Azure Virtual Machine** – Used to run and test the Flask application

All resources are grouped under a single Azure Resource Group.

---

## Application Workflow

1. User logs in using username and password
2. User creates an article with:
   - Title
   - Author
   - Body
   - Image
3. Article data is stored in Azure SQL Database
4. Image is uploaded to Azure Blob Storage
5. Article can be viewed with image rendered from Blob Storage

---

## Database Structure

- **users**
  - id
  - username
  - password

- **articles**
  - id
  - title
  - author
  - body
  - image_url

---

## Authentication

The project currently supports local username/password authentication.

Microsoft Entra ID (Azure Active Directory) authentication was explored and partially implemented during development. However, the final submitted version focuses on a stable deployment using local authentication to ensure consistent functionality.

---

## How to Run the Project

1. Create a Python virtual environment
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
