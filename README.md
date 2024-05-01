# QR Code Generator

## Deploy

1. [Install AWS SAM CLI](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/install-sam-cli.html)
1. Run `sam build --use-container && sam deploy --guided` (Make sure docker is installed and running)

## Use

1. Get a URL to create a QR code for
1. Find the API URL (see the outputs in cloud formation)
1. URL Encode the URL (You can use [this tool](https://www.urlencoder.org/))
1. In your browser, visit the API URL and add the `url` query parameter, example below:

```
https://abcde12345.execute-api.il-central-1.amazonaws.com/Prod/?url=https%3A%2F%2Fmyfavorite.com%2Flink
```
