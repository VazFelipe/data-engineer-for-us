# Contents
- [Contents](#contents)
  - [Links to the Authors That I have learned from](#links-to-the-authors-that-i-have-learned-from)
  - [A Brief Intro about Linux](#a-brief-intro-about-linux)
    - [The Growth of Linux](#the-growth-of-linux)
    - [The Linux Philosophy](#the-linux-philosophy)
    - [The Containerization of Linux](#the-containerization-of-linux)
  - [Containerization](#containerization)
    - [Simple Docker's Architecture (Client-Server) Schema](#simple-dockers-architecture-client-server-schema)
    - [What is a Container?](#what-is-a-container)
    - [What is the difference between Virtual Machines and Containers?](#what-is-the-difference-between-virtual-machines-and-containers)
    - [What is Docker?](#what-is-docker)

[Get back to the index](/README.md)

## Links to the Authors That I have learned from

- [Linode >> A Brief Intro About Linux History](https://youtu.be/f473gO3STUs?si=kNQOmhmBUJLO5x2A)
- [LINUXtips >> Containerization](https://youtu.be/MeFyp4VnNx0?si=QnlhbEbz2eWvWaqR)
- [Docker >> Simple Docker's Architecture](https://docs.docker.com/get-started/overview/#docker-architecture)

[Get back to the index](/README.md)

## A Brief Intro about Linux
### The Growth of Linux 
- **Old but Gold >> 1920s–1930s:** From telephones to telecommunications Nokia Bell Labs was the consolidation of several departments within the American Telephone & Telegraph company (AT&T) (https://www.bell-labs.com/about/history/#gref). 
- The challenge at that age was **moving from typewriter and the punch cards idea** to the computer machine that we know nowadays.
- But, main universities such as MIT, Stanford, and Pittsburgh starts building its research based on **Multics system and share computational resources** to the students connected worldwide.
- The advent of **time sharing and terminals** came as an important time in computing and in the 1960s and early 1970s CMD were developed as a time when **you had to be physically present to move data** in or out of a mainframe.
- In 1970s the developers of MIT **starts writing a simpler alternative** to Nokia Bell Labs Multics System. Then a system called UNIX (Uniplexed Information and Conputer System) was created. One of the lead developers was Dennis Richie who said **that the most important to keep** from that Multics system was not only the environment but **to encourage close communication**.
- The next decade was **the growth of UNIX** that was ported to the C language which make it extremely portable and ready to run on a variety of machines and applications. 
- During the 1980s UNIX started diverging in many ways, varying a lot on its versions, and **many companies started selling computers with different variants of UNIX**.
- In 1991 a man called **Linus Torvalds was unhappy with MS-DOS and MINIX** and developed its onw UNIX GNU licensed version named LINUX.

[Get back to the index](/README.md)

### The Linux Philosophy
- **In summary**, the connection to the birth of Linux is Bell Labs **>>** Multics **>>** QWERTY keyboards **>>** the decision for it to be an open source.
- Keep in mind that Linux was not necessarily created with the open source philosophy in mind, because the GPL license that officially made **Linux Open Source was implemented until version 0.12**.
- But how Linux became what it is known as today? The **Linux history is a long family tree that splinters of more than 600 different variations**. Those variations are called Distribuitions an anyone can contribute with the evolution.
- Around the early os **1990s three influential distros** (1990) SLS, (1992) LGX and (1993) Debian. 
- But who controls Linux in terms of license? ICANN (Internet Corporation for Assigned Names And Numbers) coordinates the URL as unique identifiers for accessing web content around the globe, and the disputes for **licensing ownership created a lot of problems**, for example brazil started creating their own linux distros in which they could control and develop then they created a dizzying array of sister projects that are essentially language adapted distros and tools that are relevant to their country of origin. 
- In the age of 2004 **it became a need to make a user-friendly version of a Linux Distro**, much of this because the philosophy of linux and maturity of the project itself that could be runned on the server side and now Linux was not easy to work for an average user.

[Get back to the index](/README.md)

### The Containerization of Linux
- Linux **need to be ready to the desktop and for both all and new computers too**. The Canonical Ubuntu is the choosen distro for the community. The market was competing and divided among several platforms and Ubuntu aimed to solve that problem. For example, LindowsOS (Linspire >> FreeSpire) was interoperable with Windows DLLs and then you could run Windows applications on top of Ubuntu.
- **Interoperability and Community was growing and in the age of 2018 the container timeline starts for Linux**, a way to ensure that a piece of software and its dependencies are packaged together so that can run anywhere (Docker, Vangrant and Kubernetes K<8>s), like in toasters, cars, siloed containers...

[Get back to the index](/README.md)

## Containerization
### Simple Docker's Architecture (Client-Server) Schema
![alt text][logo]

[logo]: https://docs.docker.com/get-started/images/docker-architecture.png

- **Docker's Client** talks to the **Docker's Host** (Docker Daemon) using its **REST API**. After this call, the host build, run and distribute your Docker containers to the **Docker's Registry**.

[Get back to the index](/README.md)

### What is a Container?

- It is a way to **isolate resources**, such as CPU, memory, disk, processes, networks, filesystem, and everything about the host.

### What is the difference between Virtual Machines and Containers?

- Let´s think about that hosts below, a server that we can do our things. We have two hosts, one for our Virtual Machines and the other for the Containers. Every host has its own **layer of hardware, operational system and the runtime**, such as Hypervisor, or Docker. In other words, we have the minimum requirements to make things work in the Virtual Machines and Container hosts.

![our_hosts](/Containers/what_is_the_difference.png)

- Inside every Virtual Machine (VM) we will need a virtualized hardware, a new operational system and a **complexity for managing it all**, like vulnerabilites.

- Inside every Container (C) we will need our application, and that's it folks 👌! And off course a degree of complexity for managing, but I think it is simpler than the other. The difference between them is **the Container share its resources** with the application.

### What is Docker?

- Docker is one of the organizations that delivers the container service, a way to isolate resources and run our applications.

- There is a book explaining way better than me, click [here](https://livro.descomplicandodocker.com.br/chapters/chapter_00.html).