# Foobar

Foobar is a Python library for dealing with word pluralization.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install foobar.

```bash
pip install foobar
```

## Usage1
design_quetionsList of microservices and port configurations are mentioned here for easy start.

```
1. Authorization service  - Running on port: 8000. Takes care of authorization, implemented via gateway server.
2. Notifications Service - Responsible for push notifications and messages to customers. Uses kafka.  
3. Gateway API server - On port 8765.
4. Zipkin distributed Server - Using kafka, distributed traces are collected and viewed.
```


1. Authorization service  - Running on port: 8000. Takes care of authorization, implemented via gateway server.
2. Notifications Service - Responsible for push notifications and messages to customers. Uses kafka.  
3. Gateway API server - On port 8765.
4. Zipkin distributed Server - Using kafka, distributed traces are collected and viewed.

1. Theatre Service - 8100, 8101.. -> Takes care of listing of available theatres based on location and movie. 
   Also responsible for listing available seats, seat pricing, show timings etc..
2. Booking Service - 8200, 8201.. -> Takes the booking details and makes a booking. Communicates with theatre service to block the seats.
   Also initiates payment and waits for completion of payment to initiate notification services.                                
3. Payment Service* - 8300, 8301.. -> Makes use of wallet ids and external payment gateway to confirm payment transaction.

1. Movie Catalogue Service* - 8080, 8081.. -> Lists out the movies available in a city.
2. Review Service: 8400 -> Stores movie reviews / CRUD operations on movie reviews / stores and calculates avg movie ratings, upvotes etc.
3. Wallet Service - 8500 -> Lists out the wallets available for a user.
4. Movie Service- 8600 -> Lists out the details of a particular movie. 	

Other tools/services:
1. Eureka Naming Server on 8765
2. Kafka
3. GitHub for collab

Thoughts for microservices:
1. Any functionality that has a faster rate of change, newer implementations etc. can be a candidate for microservice. 
For example, inventory might not change but listing/aggregation services are scalable. So Movie Service and Movie Catalogue service 
can be different.
2. Independent scalability
