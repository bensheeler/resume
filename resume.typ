#import "@preview/basic-resume:0.2.9": *

#show: resume.with(
  author: "Ben Sheeler",
  location: "Mechanicsburg, PA",
  email: "bensheeler@gmail.com",
  phone: "717-576-8947",
  accent-color: "#26428b",
  font: "Georgia",
  paper: "us-letter",
  author-position: center,
  personal-info-position: center,
)

== Work Experience

#grid(
  columns: (1fr, auto),
  [*Openlane* - Lead Software Engineer],
  [May 2026 - Present],
)
- Lead design and development on backend services that track a vehicles status within an auction lot
- Modified an iOS app to interact with a new backend service
- Built and maintained support tools written in Go and Typescript
- *Key Tech* - C\#, Pulsar, Kubernetes, Go, Typescript, Pulsar
#v(0.35em)

#grid(
  columns: (1fr, auto),
  [*Openlane* - Senior Software Engineer],
  [November 2023 - May 2026],
)
- Designed and built services and APIs in C\# /.NET to facilitate dynamic automobile inspections
- Managed terraform and kubernetes configuration for AWS deployments
- Assisted in developing the web ui using React and TypeScript
- *Key Tech* - C\#, AWS, Kubernetes, PostgreSQL, .NET, React, TypeScript
#v(0.35em)

#grid(
  columns: (1fr, auto),
  [*Amazon* - Software Engineer],
  [June 2022 - November 2023],
)
- Built a service to store SSL certificates to enable customers to inspect TLS traffic.
- Designed a new service that provides functionality to check the revocation status of SSL certificates.
- Implemented improvements to increase efficiency of the billing service by refactoring DynamoDB tables to handle large data sets. This reduced ops tickets by 15 per month.
- Fixed critical bugs in the infrastructure deployment logic to decrease deployment time by up to 2 weeks.
- *Key Tech* - Java, Python, AWS, DynamoDB
#v(0.35em)

#grid(
  columns: (1fr, auto),
  [*Omnicell* - Software Engineer 3],
  [November 2020 - June 2022],
)
- Worked on transitioning a legacy code base to a cloud based, microservice architecture using Azure, Kubernetes, and .NET which enabled increased scalability.
- Built front end web applications using Angular, Nx and Typescript, targeting multiple screen sizes and utilizing server side rendering to decrease load times by 50%.
- Developed common, shareable packages for cross team use to help decrease development time on common tasks.
- *Key Tech* - C\#, Typescript, Javascript, Angular, .NET, RabbitMQ
#v(0.35em)

#grid(
  columns: (1fr, auto),
  [*Kroll* - Senior Software Engineer],
  [September 2017 - November 2020],
)
- Led migration of applications from on prem to AWS, utilizing ec2.
- Developed a message based system using RabbitMQ to sync data in near real time between a custom application and Salesforce. Data would sync within 5 minutes.
- *Key Tech* - C\#, Javascript, Typescript, Angular, VueJS, AWS, .NET, RabbitMQ
#v(0.35em)

#grid(
  columns: (1fr, auto),
  [*Computer Aid* - Software Developer],
  [May 2014 - September 2017],
)
- Led mentorship program which consisted of training junior developers and interns using a 4-6 week project based curriculum.
- Implemented a CI and CD pipeline using Azure DevOps to reduce deployment times from 2-4 hours to 5 minutes.
- *Key Tech* - C\#, .NET, Javascript, Angular
#v(0.35em)

== Education

#edu(
  institution: "Messiah College",
  location: "Mechanicsburg, PA",
  dates: dates-helper(start-date: "August 2010", end-date: "May 2014"),
  degree: "Bachelor of Science, Computer and Information Science",
)

