# Generate the trip-check-api client from the OpenAPI Spec:
```
uv add "httpx<0.28.0,>=0.20.0" "attrs>=21.3.0" "python-dateutil<3.0.0,>=2.8.0"

uv tool install openapi-python-client
openapi-python-client generate --path tripcheck-api-v1-0.yaml --meta poetry

mv trip-check-api-v-1-client/trip_check_api_v_1_client ./trip_check_api_client
rm -r trip-check-api-v-1-client
```