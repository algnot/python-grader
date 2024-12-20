### Module 3: This is a secret

ต้นก้าต้องการ censor payload response จาก request ที่มี key ดังต่อไปนี้ `email`, `password` ตัวอย่างเช่น
```python
input = {
    "name": "Thanawat Talabtong",
    "email": "thanawat.tongla@gmail.com",
    "validator": {
        "email": "khaimook@gmail.com"
    },
    "password": "this is a password",
    "created": "2024-07-10"
}
```
โดยให้แทน value ของ key เหล่านั้นด้วย `****` แทน value เดิมจากตัวอย่างจะได้
```python
output = {
    "name": "Thanawat Talabtong",
    "email": "****",
    "validator": {
        "email": "****"
    },
    "password": "****",
    "created": "2024-07-10"
}
```

### Requirement
แก้ logic ฟังก์ชั่น `input_func(input)` โดยรับ input เป็น string ใน format json และ return ออกมาเป็น string ที่ censor payload เรียบร้อยแล้่ว

### Example Input
```python
{
    "name": "Thanawat Talabtong",
    "email": "thanawat.tongla@gmail.com",
    "password": "this is a password",
    "created": "2024-07-10"
}
```

### Example Output
```
{
    "name": "Thanawat Talabtong",
    "email": "****",
    "password": "****",
    "created": "2024-07-10"
}
```
