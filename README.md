## TodoList Smart Contract

> This is a basic Todo List Ethereum smart contract written in Solidity.

### Contract Details

The contract stores Todo items in a dynamic array `todos`.

Each Todo item has:

`text` - The text of the todo
`completed` - A boolean indicating if it's completed

### Functions

The contract exposes the following functions:

```sol
createTodo(string _text) external
```

Creates a new Todo by pushing it to the `todos` array


```sol
toggleCompleted(uint _index) external
```

Toggles the `completed` state of the Todo at the given index

```sol
deleteTodo(uint _index) external
```

Deletes the Todo from the `todos` array at the given index

```sol
getAllTodos() external view returns (Todo[] memory)
```

Returns the entire array of Todos

### Usage

This allows for a basic CRUD todo list stored on the blockchain.

The functions can be called from a Dapp frontend or through something like ethers.js.

Let me know if you have any other questions!
