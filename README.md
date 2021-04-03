# REST API
Our REST API makes use for two external APIs to deliver information for surfers for potential times when tides are high and UV index is moderate.

## External APIs
- OpenUV (UV Index Forecast)
- Stormglass (Tide forecast)

Our API implement GET, POST, PUT and DELETE methods. Following are details of API calls.
## POST
### Unsuccessful POST Request
POST request is missing one parameter 'lng' due to which server returns **HTTP/1.0 400 BAD REQUEST**
```
curl -i -H "Content-Type: application/json" -X POST -d '{"city":"Paris", "lat":"48.864716"}' http://localhost/add
```
### Successful POST Request
```
curl -i -H "Content-Type: application/json" -X POST -d '{"city":"Paris", "lat":"48.864716", "lng":"2.349014"}' http://localhost/add
```

## GET
### Successful GET Request
Returns **HTTP/1.0 200 OK**
```
curl -i http://localhost/location/paris/
```
### Usuccessful GET Request
Returns **HTTP/1.0 404 NOT FOUND**
```
curl -i http://localhost/location/newyork/
```

## PUT
### Successful PUT Request
Returns **HTTP/1.0 201 CREATED**
```
curl -i -H "Content-Type: application/json" -X PUT -d '{"city":"Paris", "lat":"51.5074", "lng":"0.1278"}' http://localhost/edit
```
### Unsuccessful PUT Request
Returns **HTTP/1.0 404 NOT FOUND**
```
curl -i -H "Content-Type: application/json" -X PUT -d '{"city":"Newyork", "lat":"51.5074", "lng":"0.1278"}' http://localhost/edit
```

## DELETE
### Successful DELETE Request
Returns **HTTP/1.0 200 OK**
```
curl -X DELETE http://localhost/delete/paris
```
### Unsuccessful DELETE Request
Returns **HTTP/1.0 404 NOT FOUND** if record does not exist in table
```
curl -X DELETE http://localhost/delete/paris
```
