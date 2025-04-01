import { Folder, File } from "lucide-react"

export default function ProjectStructure() {
  return (
    <div className="p-4 border rounded-lg bg-slate-50 dark:bg-slate-900">
      <h2 className="mb-4 text-xl font-bold">Django Project Structure</h2>
      <div className="pl-4">
        <div className="flex items-center mb-2">
          <Folder className="w-5 h-5 mr-2" />
          <span className="font-semibold">chatgpt_clone/</span> {/* Project root */}
        </div>
        <div className="pl-6">
          <div className="flex items-center mb-2">
            <Folder className="w-5 h-5 mr-2" />
            <span className="font-semibold">chatgpt_clone/</span> {/* Project settings */}
          </div>
          <div className="pl-6">
            <div className="flex items-center mb-1">
              <File className="w-5 h-5 mr-2" />
              <span>__init__.py</span>
            </div>
            <div className="flex items-center mb-1">
              <File className="w-5 h-5 mr-2" />
              <span>settings.py</span>
            </div>
            <div className="flex items-center mb-1">
              <File className="w-5 h-5 mr-2" />
              <span>urls.py</span>
            </div>
            <div className="flex items-center mb-1">
              <File className="w-5 h-5 mr-2" />
              <span>wsgi.py</span>
            </div>
            <div className="flex items-center mb-1">
              <File className="w-5 h-5 mr-2" />
              <span>asgi.py</span>
            </div>
          </div>
          <div className="flex items-center mb-2">
            <Folder className="w-5 h-5 mr-2" />
            <span className="font-semibold">chat/</span> {/* Main app */}
          </div>
          <div className="pl-6">
            <div className="flex items-center mb-1">
              <File className="w-5 h-5 mr-2" />
              <span>__init__.py</span>
            </div>
            <div className="flex items-center mb-1">
              <File className="w-5 h-5 mr-2" />
              <span>admin.py</span>
            </div>
            <div className="flex items-center mb-1">
              <File className="w-5 h-5 mr-2" />
              <span>apps.py</span>
            </div>
            <div className="flex items-center mb-1">
              <File className="w-5 h-5 mr-2" />
              <span>models.py</span>
            </div>
            <div className="flex items-center mb-1">
              <File className="w-5 h-5 mr-2" />
              <span>views.py</span>
            </div>
            <div className="flex items-center mb-1">
              <File className="w-5 h-5 mr-2" />
              <span>urls.py</span>
            </div>
            <div className="flex items-center mb-1">
              <File className="w-5 h-5 mr-2" />
              <span>forms.py</span>
            </div>
            <div className="flex items-center mb-1">
              <File className="w-5 h-5 mr-2" />
              <span>utils.py</span>
            </div>
          </div>
          <div className="flex items-center mb-2">
            <Folder className="w-5 h-5 mr-2" />
            <span className="font-semibold">static/</span>
          </div>
          <div className="pl-6">
            <div className="flex items-center mb-2">
              <Folder className="w-5 h-5 mr-2" />
              <span>css/</span>
            </div>
            <div className="flex items-center mb-2">
              <Folder className="w-5 h-5 mr-2" />
              <span>js/</span>
            </div>
            <div className="flex items-center mb-2">
              <Folder className="w-5 h-5 mr-2" />
              <span>images/</span>
            </div>
          </div>
          <div className="flex items-center mb-2">
            <Folder className="w-5 h-5 mr-2" />
            <span className="font-semibold">templates/</span>
          </div>
          <div className="pl-6">
            <div className="flex items-center mb-2">
              <Folder className="w-5 h-5 mr-2" />
              <span>chat/</span>
            </div>
            <div className="pl-6">
              <div className="flex items-center mb-1">
                <File className="w-5 h-5 mr-2" />
                <span>base.html</span>
              </div>
              <div className="flex items-center mb-1">
                <File className="w-5 h-5 mr-2" />
                <span>index.html</span>
              </div>
              <div className="flex items-center mb-1">
                <File className="w-5 h-5 mr-2" />
                <span>settings_modal.html</span>
              </div>
            </div>
          </div>
          <div className="flex items-center mb-1">
            <File className="w-5 h-5 mr-2" />
            <span>manage.py</span>
          </div>
          <div className="flex items-center mb-1">
            <File className="w-5 h-5 mr-2" />
            <span>requirements.txt</span>
          </div>
        </div>
      </div>
    </div>
  )
}

