import React, { useState } from 'react';

function ToDoList()
{
  const [tasks, setTasks] = useState(['Eat Breakfast', 'Take a shower', 'Walk the dog']);
  const [newTask, setNewTask] = useState('');

  function handleInputChange(event)
  {
    // Set the new taks's content to what is typed in the textbox.
    // This function allows me to see the content change in the textbox.

    setNewTask(event.target.value);
  }

  function addTaks()
  {
    // Check if the textbox is empty:
    if (newTask.trim() !== "")
    {
      // Add the new task to the task list:
    setTasks(t => [...t, newTask]);

    // Reset the new task field:
    setNewTask("");
    }
  }

  function deleteTask(index)
  {
    setTasks(t => t.filter((_, i) => i !== index))
  }

  function moveTaskUp(i)
  {
    // Check if the item is at the top:
    if (i > 0)
    {
      // Rearrange array using array destructuring:
      const updatedTasks = [...tasks];
      [updatedTasks[i], updatedTasks[i - 1]] = [updatedTasks[i - 1], updatedTasks[i]];

      // Update the array
      setTasks(updatedTasks);
    }
  }

  function moveTaskDown(i)
  {
    // Check if the item is at the bottom:
    if (i < (tasks.length - 1))
    {
      // Rearrange array using array destructuring:
      const updatedTasks = [...tasks];
      [updatedTasks[i], updatedTasks[i + 1]] = [updatedTasks[i + 1], updatedTasks[i]];

      // Update the array
      setTasks(updatedTasks);
    }
  }

  return(<>
    <div className='todo-list'>

      <h1 className='title'>To-Do List</h1>

      <div>
        <input type='text' placeholder='Enter a task' value={newTask}
        onChange={handleInputChange} className='textbox'/>
        <button className='add-button' onClick={addTaks}> Add task</button>
      </div>

      <ol className='todos'>
        {tasks.map((task, index) =>
          <li key={index}>

            <span className='text'>{task}</span>

            <button className='delete-button'
            onClick={() => deleteTask(index)}>Delete</button>

            <button className='move-up-button'
            onClick={() => moveTaskUp(index)}>Up</button>

            <button className='move-down-button'
            onClick={() => moveTaskDown(index)}>Down</button>

          </li>)}
      </ol>

    </div>
  </>);
}

export default ToDoList