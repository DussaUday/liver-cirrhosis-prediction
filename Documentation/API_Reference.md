# API Reference

## POST /predict
**Content-Type:** application/x-www-form-urlencoded

**Parameters:**
| Name       | Type   | Description          |
|------------|--------|----------------------|
| Age        | number | Patient age          |
| Gender     | string | Male/Female          |
| Total_Bilirubin | number | in mg/dL        |

**Response:**
```json
{
  "status": "success",
  "prediction": "High Risk",
  "confidence": 72.34,
  "timestamp": "2023-11-15T12:00:00Z"
}