## Request
```Json
{
"blocks": 7,
"intervals": 10,
"tasks": [
{
"name": "T1",
"time_blocks": 3,
"compatible_tags": ["A", "C"],
"max_per_cicle": 5,
"max_per_interval": 2
},
{
"name": "T2",
"time_blocks": 6,
"compatible_tags": ["B"],
"max_per_cicle": 7,
"max_per_interval": 3
},
{
"name": "T3",
"time_blocks": 2,
"compatible_tags": ["D", "E", "A"],
"max_per_cicle": 4,
"max_per_interval": 1
},
{
"name": "T4",
"time_blocks": 5,
"compatible_tags": ["C", "F"],
"max_per_cicle": 6,
"max_per_interval": 2
},
{
"name": "T5",
"time_blocks": 1,
"compatible_tags": ["G", "B"],
"max_per_cicle": 3,
"max_per_interval": 1
}
],
"resources": [
{
"name": "R1",
"tags": ["A", "C"],
"max_per_cicle": 6,
"max_per_interval": 2
},
{
"name": "R2",
"tags": ["B"],
"max_per_cicle": 5,
"max_per_interval": 1
},
{
"name": "R3",
"tags": ["D", "E"],
"max_per_cicle": 7,
"max_per_interval": 3
},
{
"name": "R4",
"tags": ["F", "G", "C"],
"max_per_cicle": 8,
"max_per_interval": 2
}
]
}
```

## Backend Return
```Json
{
  "blocks": 7,
  "intervals": 10,
  "heuristic": "least_blocks_max_cycle",
  "schedule": [
    [
      {
        "tasks": ["T1", "T2", "T3", "T5"],
        "resources": ["R1", "R2", "R3", "R4"]
      },
      {
        "tasks": ["T1", "T4"],
        "resources": ["R1", "R4"]
      },
      {
        "tasks": [],
        "resources": []
      },
      {
        "tasks": [],
        "resources": []
      },
      {
        "tasks": [],
        "resources": []
      },
      {
        "tasks": [],
        "resources": []
      },
      {
        "tasks": [],
        "resources": []
      },
      {
        "tasks": [],
        "resources": []
      },
      {
        "tasks": [],
        "resources": []
      },
      {
        "tasks": [],
        "resources": []
      }
    ],
    [
      {
        "tasks": ["T1", "T2", "T3", "T4"],
        "resources": ["R1", "R2", "R3", "R4"]
      },
      {
        "tasks": ["T4"],
        "resources": ["R4"]
      },
      {
        "tasks": [],
        "resources": []
      },
      {
        "tasks": [],
        "resources": []
      },
      {
        "tasks": [],
        "resources": []
      },
      {
        "tasks": [],
        "resources": []
      },
      {
        "tasks": [],
        "resources": []
      },
      {
        "tasks": [],
        "resources": []
      },
      {
        "tasks": [],
        "resources": []
      },
      {
        "tasks": [],
        "resources": []
      }
    ],
    [
      {
        "tasks": ["T2", "T4"],
        "resources": ["R2", "R4"]
      },
      {
        "tasks": ["T4"],
        "resources": ["R4"]
      },
      {
        "tasks": [],
        "resources": []
      },
      {
        "tasks": [],
        "resources": []
      },
      {
        "tasks": [],
        "resources": []
      },
      {
        "tasks": [],
        "resources": []
      },
      {
        "tasks": [],
        "resources": []
      },
      {
        "tasks": [],
        "resources": []
      },
      {
        "tasks": [],
        "resources": []
      },
      {
        "tasks": [],
        "resources": []
      }
    ],
    [
      {
        "tasks": ["T2"],
        "resources": ["R2"]
      },
      {
        "tasks": [],
        "resources": []
      },
      {
        "tasks": [],
        "resources": []
      },
      {
        "tasks": [],
        "resources": []
      },
      {
        "tasks": [],
        "resources": []
      },
      {
        "tasks": [],
        "resources": []
      },
      {
        "tasks": [],
        "resources": []
      },
      {
        "tasks": [],
        "resources": []
      },
      {
        "tasks": [],
        "resources": []
      },
      {
        "tasks": [],
        "resources": []
      }
    ],
    [
      {
        "tasks": ["T2"],
        "resources": ["R2"]
      },
      {
        "tasks": [],
        "resources": []
      },
      {
        "tasks": [],
        "resources": []
      },
      {
        "tasks": [],
        "resources": []
      },
      {
        "tasks": [],
        "resources": []
      },
      {
        "tasks": [],
        "resources": []
      },
      {
        "tasks": [],
        "resources": []
      },
      {
        "tasks": [],
        "resources": []
      },
      {
        "tasks": [],
        "resources": []
      },
      {
        "tasks": [],
        "resources": []
      }
    ],
    [
      {
        "tasks": [],
        "resources": []
      },
      {
        "tasks": [],
        "resources": []
      },
      {
        "tasks": [],
        "resources": []
      },
      {
        "tasks": [],
        "resources": []
      },
      {
        "tasks": [],
        "resources": []
      },
      {
        "tasks": [],
        "resources": []
      },
      {
        "tasks": [],
        "resources": []
      },
      {
        "tasks": [],
        "resources": []
      },
      {
        "tasks": [],
        "resources": []
      },
      {
        "tasks": [],
        "resources": []
      }
    ],
    [
      {
        "tasks": [],
        "resources": []
      },
      {
        "tasks": [],
        "resources": []
      },
      {
        "tasks": [],
        "resources": []
      },
      {
        "tasks": [],
        "resources": []
      },
      {
        "tasks": [],
        "resources": []
      },
      {
        "tasks": [],
        "resources": []
      },
      {
        "tasks": [],
        "resources": []
      },
      {
        "tasks": [],
        "resources": []
      },
      {
        "tasks": [],
        "resources": []
      },
      {
        "tasks": [],
        "resources": []
      }
    ]
  ]
}
```
