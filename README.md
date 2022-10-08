# Ciclope-Changer
![img.png](assets/img.png)
> Ciclope is an initiative of Mercado Libre infrastructure team composed of an ecosystem of microservices that together provide a software mechanism capable of switching network traffic from the main VPN to an alternative VPN.
> Cyclops Changer is a webhook responsible for receiving a request and sending a DNS record change request to the CDC service.

## Flow
![img.png](assets/flow-img.png)

## Develop Guide
The most important premise of this project is to be a continuous beta, so your contribution is very welcome.

**1. Branch Strategy**

In our project we chose to use the Gitlab **Flow strategy**, with a change in the name of the pre-production (staging) and production (main) branches.
It is worth remembering that this model is not written in stone, and suggestions are welcome.

![img.png](assets/branch-strategy-img.png)

**2. CI/CD Process**

![img.png](assets/pipelines-img.png)

**3. Local Test**

If you want to test this project locally, follow these steps:

**3.1 Build image**

```bash
docker build -t ciclope-changer:demo .
```

**3.2 Launch container**

```bash
docker run -p 80:8080 -p 8000:3000 ciclope-changer:demo
```

## Contributions

To contribute and report problems is very easy, just follow this [Doc](https://github.com/moquintanilha/ciclope-changer/blob/main/docs/contribution/README.md)

## License

© 2021 Mercado Libre
