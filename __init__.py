
# backend/long_term/__init__.py
from .contract import ALLOWED_TYPES, MIN_CONFIDENCE, DECAY_RATE, is_valid_memory
from .extractor import extract_memory, extract_name
from .store import MemoryStore
from .decay import apply_decay, refresh_memory
from .retrieval import retrieve_relevant, retrieve_by_type, get_user_name
from .injector import inject_memory_context, inject_simple, get_memory_summary
# backend/long_term/__init__.py

"""
Long-term memory system initialization
Exports all memory-related functionality
"""

from .contract import (
    ALLOWED_TYPES, MIN_CONFIDENCE, DECAY_RATE, DECAY_MULTIPLIER,
    is_valid_memory, calculate_decay_amount, should_merge_memories,
    get_memory_priority
)
from .extractor import (
    MemoryExtractor, extract_memory, extract_name, extract_multiple
)
from .store import MemoryStore
from .decay import (
    apply_decay, apply_selective_decay, refresh_memory,
    boost_related_memories, consolidate_memories,
    prune_low_priority_memories, apply_smart_decay, get_decay_stats
)
from .retrieval import (
    retrieve_relevant, retrieve_by_type, retrieve_recent,
    get_user_name, get_user_preferences, get_user_constraints,
    get_commitments, search_memories, get_memory_context_summary
)
from .injector import (
    inject_memory_context, inject_simple, inject_for_llm,
    get_memory_summary, format_memory_for_display,
    format_memories_for_display, create_memory_card
)

__all__ = [
    # Contract
    'ALLOWED_TYPES', 'MIN_CONFIDENCE', 'DECAY_RATE', 'DECAY_MULTIPLIER',
    'is_valid_memory', 'calculate_decay_amount', 'should_merge_memories',
    'get_memory_priority',
    
    # Extractor
    'MemoryExtractor', 'extract_memory', 'extract_name', 'extract_multiple',
    
    # Store
    'MemoryStore',
    
    # Decay
    'apply_decay', 'apply_selective_decay', 'refresh_memory',
    'boost_related_memories', 'consolidate_memories',
    'prune_low_priority_memories', 'apply_smart_decay', 'get_decay_stats',
    
    # Retrieval
    'retrieve_relevant', 'retrieve_by_type', 'retrieve_recent',
    'get_user_name', 'get_user_preferences', 'get_user_constraints',
    'get_commitments', 'search_memories', 'get_memory_context_summary',
    
    # Injector
    'inject_memory_context', 'inject_simple', 'inject_for_llm',
    'get_memory_summary', 'format_memory_for_display',
    'format_memories_for_display', 'create_memory_card'
]

__all__ = [
    'ALLOWED_TYPES', 'MIN_CONFIDENCE', 'DECAY_RATE', 'is_valid_memory',
    'extract_memory', 'extract_name',
    'MemoryStore',
    'apply_decay', 'refresh_memory',
    'retrieve_relevant', 'retrieve_by_type', 'get_user_name',
    'inject_memory_context', 'inject_simple', 'get_memory_summary'
]



