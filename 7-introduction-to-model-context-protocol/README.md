# [Introduction to Model Context Protocol](https://anthropic.skilljar.com/introduction-to-model-context-protocol)

without mcp

```
service                                  LLM         external
   |                                       |             |
   |------- how to do X in external ------>|             |
   |                                       |             |
   |<-------- no idea / static knowledge --|             |
   |                                       |             |
   |---                                    |             |
   |  | discover and implement             |             |
   |<--                                    |             |
   |                                       |             |
   |---------------------- call ------------------------>|
   |                                       |             |
   |<-------------------- response ----------------------|
   |                                       |             |
   |---------------------- use this ------>|             |
   |                                       |             |
   |<---------------- result---------------|             |
   |                                       |             |
```

with mcp

on session init

```
service (MCP client)              LLM              external (MCP server)
    |                              |                       |
    |------ hey external, what tools do u have ? --------->|
    |                              |                       |
    |<---------- tool definitions -------------------------|
    |                              |                       |
    |------ here are tools ------->|                       |
```

on subsequent prompt

```
service (MCP client)              LLM              external (MCP server)
    |                              |                       |
    |-- how to do X in external -->|                       |
    |                              |                       |
    |                              |---                    |
    |                              |  | this needs a tool  |
    |                              |<--                    |
    |                              |                       |
    |<------- call tool X ---------|                       |
    |                              |                       |
    |------------------ call tool X ---------------------->|
    |                              |                       |
    |<----------------- response --------------------------|
    |                              |                       |
    |----------- use this -------->|                       |
    |                              |                       |
    |<---------- result -----------|                       |
    |                              |                       |
```

[spec](https://modelcontextprotocol.io/)

most common commands:

- ListToolsRequest: what tools do u have
- ListToolsResult: here r the tools available
- CallToolRequest: i need to call tool X
- CallToolResult: here's the result of tool X
