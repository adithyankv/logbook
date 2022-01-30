# getting directories to install files in
pkgdatadir = join_paths(get_option('prefix'), get_option('datadir'), meson.project_name())
moduledir = join_paths(pkgdatadir, 'logbook')

# checking dependencies
python = import('python')

message('Looking for dependencies')
python_bin = python.find_installation('python3')
if not python_bin.found()
    error('No valid python3 binary found')
else
    message('Found python3 binary')
endif

dependency ('granite')
dependency ('gtk+-3.0')
dependency ('glib-2.0')
dependency ('gobject-2.0')

# configuring the entry point executable file
conf = configuration_data()
conf.set('PYTHON', python_bin.path())
conf.set('pkgdatadir', pkgdatadir)
configure_file(
  input: 'logbook.in',
  output: meson.project_name(),
  configuration: conf,
  install: true,
  install_dir: get_option('bindir')
)

sources = files(
    '__init__.py',
    'main.py',
    'application.py',
    'window.py',
    'headerbar.py',
    'entry_list.py',
    'entry_item.py',
    'journal_manager.py',
)

install_data(sources, install_dir: moduledir)
