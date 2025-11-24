"""Lesson 14 - Magic Methods (Solution)

Reference implementation for the Study Planner Operators exercise.
"""

class StudyBlock:
    def __init__(self, topic, minutes, notes=None):
        self.topic = topic
        self.minutes = minutes
        self.notes = notes or []

    def __repr__(self):
        return f"StudyBlock(topic={self.topic!r}, minutes={self.minutes!r}, notes={len(self.notes)} entries)"

    def __str__(self):
        return f"{self.topic} ({self.minutes} min)"

    def __len__(self):
        return self.minutes

    def __add__(self, other):
        if not isinstance(other, StudyBlock):
            return NotImplemented
        merged_notes = self.notes + other.notes
        return StudyBlock(
            topic=f"{self.topic} + {other.topic}",
            minutes=self.minutes + other.minutes,
            notes=merged_notes,
        )

    def __bool__(self):
        return self.minutes > 0


class BlockQueue:
    def __init__(self, *blocks):
        self.blocks = list(blocks)

    def __iter__(self):
        return iter(self.blocks)

    def __len__(self):
        return len(self.blocks)

    def __getitem__(self, index):
        return self.blocks[index]

    def __contains__(self, block):
        return block in self.blocks


class ProgressNotifier:
    def __call__(self, block):
        print(f"🎯 Completed {block.topic} in {block.minutes} minutes!")


# Demonstration
block_a = StudyBlock("APIs", 40, notes=["focus on GET requests"])
block_b = StudyBlock("Testing", 0, notes=["install pytest"])
block_c = StudyBlock("Dataclasses", 30)

print(block_a)
print(repr(block_b))

combo = block_a + block_c
print("Combined block:", combo)

truthy_blocks = [block for block in [block_a, block_b, block_c] if block]
print("Truthy blocks:", truthy_blocks)

queue = BlockQueue(block_a, block_b, block_c)
print("Queue length:", len(queue))
print("First entry:", queue[0])
print("Contains block_c?", block_c in queue)

notifier = ProgressNotifier()
for study_block in queue:
    notifier(study_block)
