import requests 
import jsonschema

url = 'https://reqres.in/api/users?page=2'

# отправляем GET запрос на URL
response = requests. get (url)

# проверяем статус код
if response.status_code == 200:
  print ('Статус код:', response.status code)
else:
  print('Ошибка! Статус код: ', response.status_code)

# проверяем валидность схемы JSON
schema = 4
  "type: "obiect
  properties": {
    "page": {"type": "integer"},
    "per_page": {"type": "integer"},
    "total": {"type": "integer"}, 
    "total_pages": {"type": "integer"},
    "data": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "id": {"type": "integer"},
          "email": {"type": "string"},
          "first_name": {"type": "string"},
          "last name: {"type": "string"},
          "avatar": {"type": "string"}
        },
        "required": ["id", "email", "first_name", "last_name", "avatar"]
      }
    }
  },
"required": ["page", "per_page", "total", "total_pages", "data"]
}
try:
  jsonschema.validate (response. json (), schema)
  print('Схема JSON валидна!')
except jsonchema.exceptions.ValidationError as err:
  print('Ошибка валидации схемы JSON:', err)

except jsonschema.exceptions. ValidationError as err:
print ('Ошибка валидации схемы JSON:', err)
