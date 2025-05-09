import os
import sys

# Patch pour empêcher l'import de embedchain
class EmbedChainPatch:
    def __init__(self):
        pass

    def setup(self, *args, **kwargs):
        pass

# Remplacer Client.embedchain par une version vide
sys.modules['embedchain'] = EmbedChainPatch()
sys.modules['embedchain.App'] = EmbedChainPatch()
sys.modules['embedchain.client'] = EmbedChainPatch()

# Optionnel : patcher aussi crewai.memory
try:
    import crewai.memory.storage.rag_storage
    crewai.memory.storage.rag_storage.RAGStorage = lambda *args, **kwargs: None
except:
    pass
