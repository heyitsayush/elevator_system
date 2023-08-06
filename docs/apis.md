1. Create new elevator system
    - Endpoint: ```POST  /api/v1/elevator_systems/```
    - Request body:
    ```json
    {
        "system_name": "System 1",
        "number_of_elevators": "2",
        "number_of_floors": "6"
    }
    ```
   - Response:
   ```json 
   {
        "id": 1,
        "elevators": [
            {
                "id": 1,
                "next_destination": 1,
                "elevator_number": 1,
                "current_floor": 1,
                "is_door_open": true,
                "direction": 0,
                "is_operational": true,
                "elevator_system": 1
            },
            {
                "id": 2,
                "next_destination": 1,
                "elevator_number": 2,
                "current_floor": 1,
                "is_door_open": true,
                "direction": 0,
                "is_operational": true,
                "elevator_system": 1
            }
        ],
        "system_name": "System 1",
        "number_of_elevators": 2,
        "number_of_floors": 6
    }
    ```

2. Get elevator system info
    - Endpoint: ```GET  /api/v1/elevator_systems/<system-name>```
    - Lists all the elevators in the system and their current status
   ```json
   {
       "id": 1,
       "elevators": [
           {
               "id": 1,
               "next_destination": 1,
               "elevator_number": 1,
               "current_floor": 1,
               "is_door_open": true,
               "direction": 0,
               "is_operational": true,
               "elevator_system": 1
           },
           {
               "id": 2,
               "next_destination": 1,
               "elevator_number": 2,
               "current_floor": 1,
               "is_door_open": true,
               "direction": 0,
               "is_operational": true,
               "elevator_system": 1
           }
       ],
       "system_name": "System 1",
       "number_of_elevators": 2,
       "number_of_floors": 6
   }
   ```
    
3. Create elevator request
    - Endpoint: ```POST  /api/v1/elevator_systems/<system-id>/create_elevator_request```
    - Request body:
    ```json
    {
      "requested_from_floor": 5,
      "requested_to_floor": 6
    }
    ```
   - Response:
   ```json
      {
      "elevator": 1,
      "requested_from_floor": 5,
      "requested_to_floor": 6,
      "is_serviced": true
      }
   ```
   
4. Get elevator requests
    - Endpoint: ```GET  /api/v1/elevator_systems/<system-id>/elevators/<elevator-id>/requests/```
    - Lists all the requests made to the elevator
    - Response:
    ```json
    [
        {
            "elevator": 1,
            "requested_from_floor": 2,
            "requested_to_floor": 6,
            "is_serviced": true
        },
        {
            "elevator": 1,
            "requested_from_floor": 5,
            "requested_to_floor": 6,
            "is_serviced": true
        }
    ]
    ```

5. Get elevator status
    - Endpoint: ```GET  /api/v1/elevator_systems/<system-id>/elevators/<elevator-id>/status/```
    - Responds with the current status of the elevator, current_floor, direction, next_stop, etc.
    - Response:
   ```json
    {
        "elevator_system": 1,
        "data": {
            "id": 1,
            "next_destination": 6,
            "elevator_number": 1,
            "current_floor": 6,
            "is_door_open": true,
            "direction": "1.0",
            "is_operational": true,
            "elevator_system": 1
        }
    }
    ```

6. Update elevator info
    - Endpoint: ```PATCH  /api/v1/elevator_systems/2/elevators/3/```
    - Request body:
    ```json
    {
      "id": 2,
      "elevator_number": 2,
      "current_floor": 1,
      "is_door_open": false,
      "direction": -1,
      "is_operational": false,
      "elevator_system": 1
    }
    ```
   - Response:
   ```json
    {
        "elevator_system": 1,
        "data": {
            "id": 2,
            "next_destination": 1,
            "elevator_number": 2,
            "current_floor": 1,
            "is_door_open": false,
            "direction": -1,
            "is_operational": false,
            "elevator_system": 1
        }
    }
    ```