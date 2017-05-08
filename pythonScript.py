"""
Lite install NLTK resource
"""
import nltk
dler = nltk.downloader.Downloader()
dler._update_index()
dler._status_cache['panlex_lite'] = 'installed' # Trick the index to treat panlex_lite as it's already installed.
dler.download('all')
