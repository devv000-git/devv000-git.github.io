// Historical React/Vite client structure from the VS Code project.
// This file is an educational reference. The public demo does not use it.
const BASE_URL = import.meta.env.VITE_API_BASE_URL || '';

export async function getTasks() {
  const response = await fetch(`${BASE_URL}/tasks`);
  if (!response.ok) throw new Error('Could not load tasks');
  return response.json();
}

export async function createTask(task) {
  const response = await fetch(`${BASE_URL}/tasks`, {
    method: 'POST',
    headers: {'Content-Type':'application/json'},
    body: JSON.stringify(task),
  });
  if (!response.ok) throw new Error('Could not create task');
  return response.json();
}

export async function updateTask(id, task) {
  const response = await fetch(`${BASE_URL}/tasks/${id}`, {
    method: 'PUT',
    headers: {'Content-Type':'application/json'},
    body: JSON.stringify(task),
  });
  if (!response.ok) throw new Error('Could not update task');
  return response.json();
}

export async function deleteTask(id) {
  const response = await fetch(`${BASE_URL}/tasks/${id}`, { method:'DELETE' });
  if (!response.ok) throw new Error('Could not delete task');
}

// Security note: The historical prototype lacked authenticated API access.
// Do not connect this browser client directly to a live unprotected API.
