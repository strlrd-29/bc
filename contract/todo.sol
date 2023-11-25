// SPDX-License-Identifier: UNLICENSED
pragma solidity ^0.8.0;

contract TodoList {

    struct Todo {
        string text;
        bool completed;
    }

    Todo[] public todos;

    function createTodo(string calldata _text) external {
        todos.push(Todo(_text, false));
    }

    function toggleCompleted(uint _index) external {
        Todo storage todo = todos[_index];
        todo.completed = !todo.completed;
    }

    function deleteTodo(uint _index) external {
        delete todos[_index];
    }

    function getAllTodos() external view returns (Todo[] memory) {
        return todos;
    }
}
