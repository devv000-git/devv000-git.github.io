/**
 * Selected React logic adapted from the private VS Code placement project.
 * This example receives its data API as a dependency so it is not connected
 * to the historical anonymous Azure backend.
 *
 * The original full App.jsx is included in the sanitised source ZIP shared
 * privately with the portfolio owner. This is a shorter public excerpt.
 */
import React, { useEffect, useMemo, useState } from 'react';

const SKILLS = [
  'Technical Literacy', 'Technical Impact', 'Ethical Obligations',
  'Professional Standards', 'Professional Communication',
  'Technical Writing and Documentation', 'Problem Analysis and Research',
  'Problem Solution Development', 'Teamwork and Collaboration',
  'Adaptability'
];
const blank = {
  date: '', hours: 1, title: '', category: 'Azure / Cloud',
  status: 'Completed', what: '', soWhat: '', nowWhat: '', skills: []
};

export default function TaskDashboardExcerpt({ api }) {
  const [tasks, setTasks] = useState([]);
  const [form, setForm] = useState(blank);
  const [editingId, setEditingId] = useState(null);
  const [error, setError] = useState('');
  const [loading, setLoading] = useState(true);

  async function refresh() {
    setLoading(true);
    try {
      setTasks(await api.getTasks());
      setError('');
    } catch (err) {
      setError(err.message);
    } finally {
      setLoading(false);
    }
  }
  useEffect(() => { refresh(); }, [api]);

  const totalHours = useMemo(
    () => tasks.reduce((sum, task) => sum + Number(task.hours || 0), 0),
    [tasks]
  );
  const completed = useMemo(
    () => tasks.filter(task => task.status === 'Completed').length,
    [tasks]
  );
  const progress = Math.min(100, Math.round(totalHours));

  function toggleSkill(skill) {
    setForm(current => ({
      ...current,
      skills: current.skills.includes(skill)
        ? current.skills.filter(item => item !== skill)
        : [...current.skills, skill]
    }));
  }

  async function submit(event) {
    event.preventDefault();
    if (!form.title.trim()) return;
    try {
      const data = { ...form, hours: Number(form.hours) };
      if (editingId) await api.updateTask(editingId, data);
      else await api.createTask(data);
      setEditingId(null);
      setForm(blank);
      await refresh();
    } catch (err) { setError(err.message); }
  }
  async function remove(id) {
    if (!window.confirm('Delete this task?')) return;
    try {
      await api.deleteTask(id);
      await refresh();
    } catch (err) { setError(err.message); }
  }

  return <main>
    <h1>Placement Dashboard</h1>
    <p>Recorded hours: {totalHours.toFixed(1)} / 100</p>
    <p>Completed activities: {completed} / {tasks.length}</p>
    <progress value={progress} max={100}>{progress}%</progress>
    {error && <p role="alert">{error}</p>}
    <form onSubmit={submit}>
      <label>Activity title <input value={form.title} required
        onChange={e => setForm({ ...form, title: e.target.value })}/></label>
      <label>Hours <input type="number" min="0.25" max="24" step="0.25"
        value={form.hours} onChange={e => setForm({ ...form, hours: e.target.value })}/></label>
      {['what','soWhat','nowWhat'].map(key =>
        <label key={key}>{key === 'what' ? 'WHAT' : key === 'soWhat' ? 'SO WHAT' : 'NOW WHAT'}
          <textarea value={form[key]} onChange={e => setForm({ ...form, [key]: e.target.value })}/>
        </label>
      )}
      <fieldset><legend>Skills</legend>
        {SKILLS.map(skill => <label key={skill}>
          <input type="checkbox" checked={form.skills.includes(skill)}
            onChange={() => toggleSkill(skill)}/> {skill}
        </label>)}
      </fieldset>
      <button type="submit">{editingId ? 'Update' : 'Create'} activity</button>
      {editingId && <button type="button" onClick={() => {setEditingId(null);setForm(blank);}}>Cancel</button>}
    </form>
    <section aria-label="Placement tasks">
      {loading ? <p>Loading...</p> : tasks.map(task =>
        <article key={task.id}>
          <h2>{task.title}</h2><p>{task.date} · {task.hours} hours</p>
          <p>WHAT: {task.what}</p><p>SO WHAT: {task.soWhat}</p><p>NOW WHAT: {task.nowWhat}</p>
          <button type="button" onClick={() => {setEditingId(task.id);setForm({...blank,...task});}}>Edit</button>
          <button type="button" onClick={() => remove(task.id)}>Delete</button>
        </article>
      )}
    </section>
  </main>;
}
