def get_json_object_example():
    return '''{
  "stop": {
    "id": "8501120",
    "name": "Lausanne",
    "type": "train,strain",
    "x": "537875",
    "y": "152042",
    "lon": 6.629087,
    "lat": 46.516795
  },
  "connections": [
    {
      "time": "2024-01-12 00:02:00",
      "*G": "R",
      "*L": "4",
      "*Z": "024492",
      "type": "train",
      "line": "R",
      "operator": "SBB",
      "color": "039~fff~",
      "type_name": "Railway",
      "terminal": {
        "id": "8501103",
        "name": "Vallorbe",
        "x": 518333,
        "y": 174024,
        "lon": 6.370564,
        "lat": 46.712419
      },
      "track": "81DG",
      "subsequent_stops": [
        {
          "id": "8518452",
          "name": "Prilly-Malley",
          "x": 535856,
          "y": 153164,
          "lon": 6.602624,
          "lat": 46.526697,
          "arr": "1970-01-01 00:05:00",
          "dep": "1970-01-01 00:06:00"
        },
        {
          "id": "8501118",
          "name": "Renens VD",
          "x": 534051,
          "y": 154334,
          "lon": 6.578933,
          "lat": 46.537046,
          "arr": "1970-01-01 00:08:00",
          "dep": "1970-01-01 00:08:00"
        },
        {
          "id": "8501117",
          "name": "Bussigny",
          "x": 531985,
          "y": 155530,
          "lon": 6.551827,
          "lat": 46.547598,
          "arr": "1970-01-01 00:11:00",
          "dep": "1970-01-01 00:11:00"
        }
      ]
    }
  ],
  "request": null,
  "eof": 1
}'''