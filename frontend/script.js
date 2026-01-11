const API = "http://localhost:30002/tasks";

        async function loadTasks()
        {
            try 
            {
                const res = await fetch(API);
                const data = await res.json();
                const list = document.getElementById('taskList');
                list.innerHTML = data.map(t => `<li>${t.title}</li>`).join('');
            } 
            catch(err) 
            { 
                console.error("Error loading: ", err); 
            }
        }

        async function addTask() 
        {
            const input = document.getElementById('taskInput');
            if(!input.value) return;
            
            await fetch(API, {
                method: 'POST',
                headers: {'Content-Type': 'application/json'},
                body: JSON.stringify({title: input.value})
            });
            input.value = '';
            loadTasks();
        }
        async function DeleteTask() 
        {
            if(confirm("Delete all")) 
            {
                try 
                {
                    await fetch(API, { method: 'DELETE' });
                    loadTasks();
                } 
                catch (err) 
                { 
                    console.error("Error deleting:", err); 
                }
            }
        }

        loadTasks();