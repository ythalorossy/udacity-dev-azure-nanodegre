# Udacity - Azure Developer Nanodegree
## Nanodegree with a focus in Azure Development, infrastructure, and deployment

Learn to build cloud-based applications on Microsoft Azure

## Modules

### Azure Application
In this course, you will learn the basics of deploying an application to Azure and understand the benefits and costs of cloud deployments, different types of service models, and how to navigate the Microsoft Azure platform.

#### Project 01

In this project, you will deploy an article content management system (CMS), built with a Python Flask application, to Microsoft Azure. The CMS system lets a user log in, view published articles, and publish new articles. First, you will deploy storage solutions for the application to interact with, such as a SQL database that contains a user table and an article table for the webapp to query, along with a Blob Storage container where images are stored. In addition to a simple username/password login, you will then need to add an option to "Sign in with Microsoft" for authentication using OAuth 2.0 and Azure Active Directory. Lastly, you will add logging to the cloud application to be able to track successful or unsuccessful login attempts. 

### Azure Microservices

In this course, you will learn how to implement a serverless microservice back-end architecture in Python using Azure cloud serverless offerings. You’ll compare and contrast common Azure microservices architecture and compute options, configure an instance of a MongoDB database with Azure Cosmos DB, and allow the API to talk to this database. You will also apply Enterprise Logic Apps and Event Grid to structure an application workflow. Finally, you’ll deploy published API endpoints so they provide the necessary responses to complete the client-side requests of the front-end web application.

#### Project 02

In this project, you will implement a serverless microservice back-end architecture for a social networking web application called Neighborly, a service for neighbors to exchange helpful information, goods, and services. First, you’ll build the back-end services that leverage an API to communicate with a MongoDB database. Then, you'll integrate the client-side application and server-side API endpoints in Python. You'll finish by deploying and managing their service with AKS for future CI/CD integration.

### Azure Migration

This course focuses on the techniques, processes, and nuances of migrating an existing application to Azure. It will cover the whole end-to-end process of an Azure migration from predicting costs of the migration to refactoring the code to ensure the application and corresponding databases are compatible with Azure. In addition, the course walks through best practices of the different application components migrated to Azure: web applications, background processes, and databases.

#### Project 03

You will strategically migrate a pre-existing conference registration system to Azure. Taking in consideration cost, you will architect a resilient and scalable system in Azure with the knowledge that the legacy application is very expensive, unable to scale at peak, has one single point of failure and performance issues, and is underutilized during off hours. First, you’ll migrate and deploy the pre-existing web app to an Azure App Service. Then, you’ll migrate a PostgreSQL database backup to an Azure Postgres database instance. Finally, you will refactor the notification logic to an Azure Function via a service bus queue message.

### Azure Performance

This course enables students to acquire skills which allow them to collect data about the health and performance of an application, analyze and display the collected data to make informed decisions, and create automation to remedy application health or performance issues. You will set up and use Application Insights on a variety of Azure resources, and use the Application Insights SDK in a Python application to collect and transmit data about the application. You’ll also query, transform, and display the collected application data so that the data can easily be analyzed, and use automation in Azure to manage cloud resources.

#### Project 04

In this project, you will collect and display performance and health data about an application post-migration to Azure. First, you’ll set up Application Insights monitoring on a virtual machine scale set (VMSS) and implement monitoring in an application to collect telemetry data. Then you will create auto-scaling for a VMSS and an Azure Automation account to create a RunBook that automates the resolution of performance issues. Finally, you’ll create alerts to trigger auto-scaling on an Azure Kubernetes Service (AKS) cluster and trigger a Runbook to execute.
