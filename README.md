# REST API
Our REST API makes use for two external APIs to deliver information for surfers for potential times when tides are high and UV index is moderate.

## External APIs
- OpenUV (UV Index Forecast)
- Stormglass (Tide forecast)

Our API implement GET, POST, PUT and DELETE methods. Following are details of API calls.
## POST
### CREATE City (Only user with admin role)
### Unsuccessful POST Request
POST request is missing one parameter 'lng' due to which server returns **HTTP/1.0 400 BAD REQUEST**
```
curl -u mehwish:qmul123 -i -H "Content-Type: application/json" -X POST -d '{"city":"Paris", "lat":"48.864716"}' http://localhost/add
```
### UNAUTHORIZED ACCESS
POST request with missing credientails or non admin user will serve unauthorized access error
```
curl -i -H "Content-Type: application/json" -X POST -d '{"city":"Paris", "lat":"48.864716", "lng":"2.349014"}' http://localhost/add
```
### Successful POST Request
```
curl -u mehwish:qmul123 -i -H "Content-Type: application/json" -X POST -d '{"city":"Paris", "lat":"48.864716", "lng":"2.349014"}' http://localhost/add
```
```
curl -u mehwish:qmul123 -i -H "Content-Type: application/json" -X POST -d '{"userName":"mehwish", "password":"qmul123", "role":"2.349014"}' http://localhost/add
```
### CREATE USER (Only user with admin role)
### Successful POST Request 
```
curl -u mehwish:qmul123 -i -H "Content-Type: application/json" -X POST -d "{"userName":"Moee", "password":"qmul123", "role":"admin"}" http://localhost/add_user
```

## GET
### Successful GET Request
Returns **HTTP/1.0 200 OK**
```
curl -u mehwish:qmul123 -i http://localhost/location/paris/
```
### Usuccessful GET Request
when data doesn't exits
Returns **HTTP/1.0 404 NOT FOUND**
```
curl -u mehwish:qmul123 -i http://localhost/location/newyork/
```
### UNAUTHORIZED ACCESS
POST request with missing credientails or non admin user will serve unauthorized access error
```
curl -i http://localhost/location/newyork/
```
## PUT
### Successful PUT Request
Returns **HTTP/1.0 201 CREATED**
```
curl -u mehwish:qmul123 -i -H "Content-Type: application/json" -X PUT -d '{"city":"Paris", "lat":"51.5074", "lng":"0.1278"}' http://localhost/edit
```
### Unsuccessful PUT Request
Returns **HTTP/1.0 404 NOT FOUND**
```
curl -u mehwish:qmul123 -i -H "Content-Type: application/json" -X PUT -d '{"city":"Newyork", "lat":"51.5074", "lng":"0.1278"}' http://localhost/edit
```
### UNAUTHORIZED ACCESS
PUT request with missing credientails or non admin user will serve unauthorized access error
```
curl -i -H "Content-Type: application/json" -X PUT -d '{"city":"Paris", "lat":"51.5074", "lng":"0.1278"}' http://localhost/edit
```
## DELETE
### Successful DELETE Request
Returns **HTTP/1.0 200 OK**
```
curl -u mehwish:qmul123 -X DELETE http://localhost/delete/paris
```
### Unsuccessful DELETE Request
Returns **HTTP/1.0 404 NOT FOUND** if record does not exist in table
```
curl -u mehwish:qmul123 -X DELETE http://localhost/delete/paris
```
### UNAUTHORIZED ACCESS
DELETE request with missing credientails or non admin user will serve unauthorized access error
```
curl -X DELETE http://localhost/delete/paris
```