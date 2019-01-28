#### application/x-www-form-urlencoded

默认类型，跟GET参数类似，会做urlencode

```
Content-Type: application/x-www-form-urlencoded

name=todd&age=12
```

#### application/form-data

可以上传文件，在Content-Type里使用boundary分割数据

```
Content-Type: multipart/form-data; boundary=---WebKitFormBoundary7MA4YWxkTrZu0gW

------WebKitFormBoundary7MA4YWxkTrZu0gW
Content-Disposition: form-data; name="name"

todd
------WebKitFormBoundary7MA4YWxkTrZu0gW
Content-Disposition: form-data; name="age"

12
```

#### application/json

```
Content-Type: application/json

{"name":"todd","age":12}
```