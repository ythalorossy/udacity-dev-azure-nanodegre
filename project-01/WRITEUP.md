# Write-up Template

## Analyze, choose, and justify the appropriate resource option for deploying the app.

*For **both** a VM or App Service solution for the CMS app:*
- *Analyze costs, scalability, availability, and workflow*
- *Choose the appropriate solution (VM or App Service) for deploying the app*
- *Justify your choice*

### Decissions and Comparisons

#### Virtual Machines

I already have an application running internally. The planning is initially to `migrate` from `bare-metal` machines to `Virtual Machines` in the cloud.

Software developers team, and infrastructure team, already have experience with the maintenance of the environment, building, continuous integration, and deployment processes.

Even though Virtual Machine is more expensive than App Service, it will be cheaper to maintain the application in the cloud than in bare-metal machines.

### Comparison between Virtual Machines and App Service

#### Price
`Virtual Machine` is more expensive than `App Service` because it is still running, consuming resources, like CPU and memory, even though when the application is not in use. 

Often to use the `App service` is necessary to pay for a plan. Using the `Virtual Machine` you should pay for usage (pay-as-you-go).  

#### Scalability
`Azure App Service` has constraints in terms of scalability.
`Azure VMs` are preferred for apps, which have the scope to expand for the future.

#### Maintenance
`Virtual Machine` requires much more time and maintenance than App Services. Using `App service`, developers only need to focus int the technologies used on the application.
`Virtual Machine` is much better for applications that need more maintainability and changes.

#### Effort to developing an application
Using `App Service` is much simpler and faster than developing using `Virtual Machines` 

## Assess app changes that would change your decision.
*Detail how the app and any other needs would have to change for you to change your decision in the last section.* 

Given that the application was already `running for many years`, `the environment` and the machines were completely `adapted for the application needs`. To migrate from a bare-metal environment to a VM in the cloud, the team will `need to re-create the environment inside the VM`. The recreation implies in reinstall the operation system, platform and middlewares to support the application, libraries, and frameworks.

In terms of the application, I believe that some changes to optimize the consumption of a resource, like memory, CPU, avoid intensive IO and improve some cache technologies. These changes are necessary because before the migration the application never considered the consumption of resources.

After the migration should be interesting to identify which part of the application can be converted into a module, or service, maybe to be deployed as an `App Service`. 


