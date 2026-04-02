LOCATION_SCHEMA = {
    "type": "object",
    "required": ["pathParameters"],
    "properties": {
        "pathParameters": {
            "type": "object",
            "required": ["location"],
            "properties": {
                "location": {
                    "type": "string",
                },
            },
        },
    },
}
