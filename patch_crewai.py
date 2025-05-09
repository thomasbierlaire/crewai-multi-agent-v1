import sys

# Patch pour embedchain
class DummyEmbedChain:
    def __init__(self, *args, **kwargs):
        pass

    def __getattr__(self, item):
        return DummyEmbedChain

    def __call__(self, *args, **kwargs):
        return DummyEmbedChain()

# Remplacer tous les modules mémoire
def dummy_module():
    return DummyEmbedChain()

sys.modules['embedchain'] = DummyEmbedChain()
sys.modules['embedchain.App'] = DummyEmbedChain()
sys.modules['crewai.memory.storage.rag_storage'] = DummyEmbedChain()
sys.modules['crewai.memory.entity.entity_memory_item'] = DummyEmbedChain()
sys.modules['crewai.memory.long_term.long_term_memory_item'] = DummyEmbedChain()
sys.modules['crewai.memory.contextual.contextual_memory_item'] = DummyEmbedChain()
sys.modules['crewai.memory.entity.entity_memory'] = DummyEmbedChain()
sys.modules['crewai.memory.long_term.long_term_memory'] = DummyEmbedChain()
sys.modules['crewai.memory.contextual.contextual_memory'] = DummyEmbedChain()
sys.modules['crewai.agents.cache_handler'] = DummyEmbedChain()
sys.modules['crewai.agents.tools_handler'] = DummyEmbedChain()
