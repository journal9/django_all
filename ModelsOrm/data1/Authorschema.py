author_schema={
    "name":"Author",
    "properties":{
        "name":{
            "type":"string",
            "maxLength":30
        },
        "experience":{
            "type":"integer",
            "maximum":80
        }
    }
}

book_schema={
    "name":"Book",
    "properties":{
        "author":{
            "type":"string",
            "maxLength":30
        },
        "title":{
            "type":"string",
            "maxLength":50
        },
        "pages":{
            "type":"integer",
            "maximum":4000
        },
        "price":{
            "type":"integer",
            "minimum":1
        },
        "start_date": {
            "type":"string",
            "pattern":'^[0-9]{2}-[0-9]{2}-[0-9]{4}$'
         },
        "published_date": {
            "type":"string",
            "pattern":'^[0-9]{4}-[0-9]{2}-[0-9]{2}$'
         },
        "updated_at": {
            "type":"string",
            "pattern":'^[0-9]{2}-[0-9]{2}-[0-9]{4}$'
         },
        "reach":{
            "type":"string"
        },
        "rating":{
            "type":"number"
        }
    }
}