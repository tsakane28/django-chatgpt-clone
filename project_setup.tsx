import { Tabs, TabsContent, TabsList, TabsTrigger } from "@/components/ui/tabs"

export default function ProjectSetup() {
  return (
    <div className="p-4 border rounded-lg bg-slate-50 dark:bg-slate-900">
      <h2 className="mb-4 text-xl font-bold">Project Setup Instructions</h2>

      <Tabs defaultValue="setup">
        <TabsList>
          <TabsTrigger value="setup">Initial Setup</TabsTrigger>
          <TabsTrigger value="run">Run Project</TabsTrigger>
        </TabsList>

        <TabsContent value="setup" className="p-4 border rounded-lg mt-2">
          <ol className="space-y-2 list-decimal list-inside">
            <li>
              Create a virtual environment:
              <div className="p-2 mt-1 font-mono text-sm bg-black text-white rounded">python -m venv venv</div>
            </li>
            <li>
              Activate the virtual environment:
              <div className="p-2 mt-1 font-mono text-sm bg-black text-white rounded">
                # On Windows
                <br />
                venv\Scripts\activate
                <br />
                <br /># On macOS/Linux
                <br />
                source venv/bin/activate
              </div>
            </li>
            <li>
              Install the required packages:
              <div className="p-2 mt-1 font-mono text-sm bg-black text-white rounded">
                pip install -r requirements.txt
              </div>
            </li>
            <li>
              Create the Django project:
              <div className="p-2 mt-1 font-mono text-sm bg-black text-white rounded">
                django-admin startproject chatgpt_clone
              </div>
            </li>
            <li>
              Create the chat app:
              <div className="p-2 mt-1 font-mono text-sm bg-black text-white rounded">
                cd chatgpt_clone
                <br />
                python manage.py startapp chat
              </div>
            </li>
            <li>
              Apply migrations:
              <div className="p-2 mt-1 font-mono text-sm bg-black text-white rounded">
                python manage.py makemigrations
                <br />
                python manage.py migrate
              </div>
            </li>
          </ol>
        </TabsContent>

        <TabsContent value="run" className="p-4 border rounded-lg mt-2">
          <ol className="space-y-2 list-decimal list-inside">
            <li>
              Run the development server:
              <div className="p-2 mt-1 font-mono text-sm bg-black text-white rounded">python manage.py runserver</div>
            </li>
            <li>
              Open your browser and navigate to:
              <div className="p-2 mt-1 font-mono text-sm bg-black text-white rounded">http://127.0.0.1:8000/</div>
            </li>
          </ol>
        </TabsContent>
      </Tabs>
    </div>
  )
}

