# Generated by the protocol buffer compiler.  DO NOT EDIT!

from google.protobuf import descriptor
from google.protobuf import message
from google.protobuf import reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)


DESCRIPTOR = descriptor.FileDescriptor(
  name='Hero.proto',
  package='D3.Hero',
  serialized_pb='\n\nHero.proto\x12\x07\x44\x33.Hero\x1a\x19\x41ttributeSerializer.proto\x1a\x0eHireling.proto\x1a\x0bItems.proto\x1a\x13OnlineService.proto\"\\\n\nVisualItem\x12\x0c\n\x04gbid\x18\x01 \x01(\x0f\x12\x10\n\x08\x64ye_type\x18\x02 \x01(\x11\x12\x18\n\x10item_effect_type\x18\x03 \x01(\x11\x12\x14\n\x0c\x65\x66\x66\x65\x63t_level\x18\x04 \x01(\x11\";\n\x0fVisualEquipment\x12(\n\x0bvisual_item\x18\x01 \x03(\x0b\x32\x13.D3.Hero.VisualItem\":\n\x11QuestHistoryEntry\x12\x11\n\tsno_quest\x18\x01 \x02(\x0f\x12\x12\n\ndifficulty\x18\x02 \x02(\x11\"R\n\x17QuestRewardHistoryEntry\x12\x11\n\tsno_quest\x18\x01 \x02(\x0f\x12\x10\n\x08step_uid\x18\x02 \x02(\x11\x12\x12\n\ndifficulty\x18\x03 \x02(\x11\"\xc5\x03\n\x06\x44igest\x12\x0f\n\x07version\x18\x01 \x02(\r\x12+\n\x07hero_id\x18\x02 \x02(\x0b\x32\x1a.D3.OnlineService.EntityId\x12\x11\n\thero_name\x18\x03 \x02(\t\x12\x12\n\ngbid_class\x18\x04 \x02(\x0f\x12\r\n\x05level\x18\x05 \x02(\x11\x12\x14\n\x0cplayer_flags\x18\x06 \x02(\r\x12\x32\n\x10visual_equipment\x18\x07 \x02(\x0b\x32\x18.D3.Hero.VisualEquipment\x12\x31\n\rquest_history\x18\x08 \x03(\x0b\x32\x1a.D3.Hero.QuestHistoryEntry\x12\x17\n\x0flast_played_act\x18\n \x02(\x11\x12\x1c\n\x14highest_unlocked_act\x18\x0b \x02(\x11\x12\x1e\n\x16last_played_difficulty\x18\x0c \x02(\x11\x12#\n\x1bhighest_unlocked_difficulty\x18\r \x02(\x11\x12\x19\n\x11last_played_quest\x18\x0e \x02(\x0f\x12\x1e\n\x16last_played_quest_step\x18\x0f \x02(\x11\x12\x13\n\x0btime_played\x18\x10 \x02(\r\"8\n\x10HotbarButtonData\x12\x11\n\tsno_power\x18\x01 \x02(\x0f\x12\x11\n\tgbid_item\x18\x02 \x02(\x0f\"M\n\x0fSkillKeyMapping\x12\x11\n\tsno_power\x18\x01 \x02(\x0f\x12\x11\n\tid_hotkey\x18\x02 \x02(\x11\x12\x14\n\x0cskill_button\x18\x03 \x02(\x11\"\x87\x01\n\nSavedQuest\x12\x11\n\tsno_quest\x18\x01 \x02(\x0f\x12\x12\n\ndifficulty\x18\x02 \x02(\x11\x12\x18\n\x10\x63urrent_step_uid\x18\x03 \x02(\x11\x12\x17\n\x0fobjective_state\x18\x04 \x03(\x11\x12\x1f\n\x17\x66\x61ilure_condition_state\x18\x05 \x03(\x11\"\'\n\x0bLearnedLore\x12\x18\n\x10sno_lore_learned\x18\x01 \x03(\x0f\"\\\n\x12SavedConversations\x12%\n\x1dplayed_conversations_bitfield\x18\x01 \x02(\x0c\x12\x1f\n\x17sno_saved_conversations\x18\x02 \x03(\x0f\"Z\n\x13SavePointData_Proto\x12\x11\n\tsno_world\x18\x01 \x02(\x0f\x12\x18\n\x10savepoint_number\x18\x02 \x02(\x11\x12\x16\n\x0e\x63reates_portal\x18\x03 \x02(\r\"\xd9\x03\n\tSavedData\x12<\n\x19hotbar_button_assignments\x18\x01 \x03(\x0b\x32\x19.D3.Hero.HotbarButtonData\x12/\n\rskill_key_map\x18\x02 \x03(\x0b\x32\x18.D3.Hero.SkillKeyMapping\x12\x13\n\x0btime_played\x18\x03 \x02(\r\x12\x1b\n\x13\x61\x63tivated_waypoints\x18\x04 \x02(\r\x12\x33\n\x13hireling_saved_data\x18\x05 \x02(\x0b\x32\x16.D3.Hireling.SavedData\x12\x17\n\x0flast_level_time\x18\x06 \x02(\r\x12*\n\x0clearned_lore\x18\x07 \x02(\x0b\x32\x14.D3.Hero.LearnedLore\x12\x38\n\x13saved_conversations\x18\x08 \x02(\x0b\x32\x1b.D3.Hero.SavedConversations\x12\x19\n\x11sno_active_skills\x18\t \x03(\x0f\x12\x12\n\nsno_traits\x18\n \x03(\x0f\x12\x16\n\x0eseen_tutorials\x18\x0b \x03(\x0f\x12\x30\n\nsave_point\x18\x0c \x02(\x0b\x32\x1c.D3.Hero.SavePointData_Proto\"6\n\nTimestamps\x12\x13\n\x0b\x63reate_time\x18\x01 \x02(\x12\x12\x13\n\x0b\x64\x65lete_time\x18\x02 \x01(\x12\"\xbb\x02\n\x0fSavedDefinition\x12\x0f\n\x07version\x18\x01 \x02(\r\x12\x1f\n\x06\x64igest\x18\x02 \x01(\x0b\x32\x0f.D3.Hero.Digest\x12\x41\n\x10saved_attributes\x18\x03 \x02(\x0b\x32\'.D3.AttributeSerializer.SavedAttributes\x12&\n\nsaved_data\x18\x04 \x01(\x0b\x32\x12.D3.Hero.SavedData\x12(\n\x0bsaved_quest\x18\x05 \x03(\x0b\x32\x13.D3.Hero.SavedQuest\x12!\n\x05items\x18\x06 \x01(\x0b\x32\x12.D3.Items.ItemList\x12>\n\x14quest_reward_history\x18\x07 \x03(\x0b\x32 .D3.Hero.QuestRewardHistoryEntry\" \n\x0cNameSequence\x12\x10\n\x08sequence\x18\x01 \x01(\x03\"\x18\n\x08NameText\x12\x0c\n\x04name\x18\x01 \x02(\t\"w\n\x06\x45scrow\x12\x0f\n\x07version\x18\x01 \x02(\r\x12&\n\tgenerator\x18\x02 \x01(\x0b\x32\x13.D3.Items.Generator\x12%\n\thero_data\x18\x03 \x01(\x0b\x32\x12.D3.Hero.SavedData\x12\r\n\x05state\x18\x04 \x01(\r')




_VISUALITEM = descriptor.Descriptor(
  name='VisualItem',
  full_name='D3.Hero.VisualItem',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='gbid', full_name='D3.Hero.VisualItem.gbid', index=0,
      number=1, type=15, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='dye_type', full_name='D3.Hero.VisualItem.dye_type', index=1,
      number=2, type=17, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='item_effect_type', full_name='D3.Hero.VisualItem.item_effect_type', index=2,
      number=3, type=17, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='effect_level', full_name='D3.Hero.VisualItem.effect_level', index=3,
      number=4, type=17, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=100,
  serialized_end=192,
)


_VISUALEQUIPMENT = descriptor.Descriptor(
  name='VisualEquipment',
  full_name='D3.Hero.VisualEquipment',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='visual_item', full_name='D3.Hero.VisualEquipment.visual_item', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=194,
  serialized_end=253,
)


_QUESTHISTORYENTRY = descriptor.Descriptor(
  name='QuestHistoryEntry',
  full_name='D3.Hero.QuestHistoryEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='sno_quest', full_name='D3.Hero.QuestHistoryEntry.sno_quest', index=0,
      number=1, type=15, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='difficulty', full_name='D3.Hero.QuestHistoryEntry.difficulty', index=1,
      number=2, type=17, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=255,
  serialized_end=313,
)


_QUESTREWARDHISTORYENTRY = descriptor.Descriptor(
  name='QuestRewardHistoryEntry',
  full_name='D3.Hero.QuestRewardHistoryEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='sno_quest', full_name='D3.Hero.QuestRewardHistoryEntry.sno_quest', index=0,
      number=1, type=15, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='step_uid', full_name='D3.Hero.QuestRewardHistoryEntry.step_uid', index=1,
      number=2, type=17, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='difficulty', full_name='D3.Hero.QuestRewardHistoryEntry.difficulty', index=2,
      number=3, type=17, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=315,
  serialized_end=397,
)


_DIGEST = descriptor.Descriptor(
  name='Digest',
  full_name='D3.Hero.Digest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='version', full_name='D3.Hero.Digest.version', index=0,
      number=1, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='hero_id', full_name='D3.Hero.Digest.hero_id', index=1,
      number=2, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='hero_name', full_name='D3.Hero.Digest.hero_name', index=2,
      number=3, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='gbid_class', full_name='D3.Hero.Digest.gbid_class', index=3,
      number=4, type=15, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='level', full_name='D3.Hero.Digest.level', index=4,
      number=5, type=17, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='player_flags', full_name='D3.Hero.Digest.player_flags', index=5,
      number=6, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='visual_equipment', full_name='D3.Hero.Digest.visual_equipment', index=6,
      number=7, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='quest_history', full_name='D3.Hero.Digest.quest_history', index=7,
      number=8, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='last_played_act', full_name='D3.Hero.Digest.last_played_act', index=8,
      number=10, type=17, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='highest_unlocked_act', full_name='D3.Hero.Digest.highest_unlocked_act', index=9,
      number=11, type=17, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='last_played_difficulty', full_name='D3.Hero.Digest.last_played_difficulty', index=10,
      number=12, type=17, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='highest_unlocked_difficulty', full_name='D3.Hero.Digest.highest_unlocked_difficulty', index=11,
      number=13, type=17, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='last_played_quest', full_name='D3.Hero.Digest.last_played_quest', index=12,
      number=14, type=15, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='last_played_quest_step', full_name='D3.Hero.Digest.last_played_quest_step', index=13,
      number=15, type=17, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='time_played', full_name='D3.Hero.Digest.time_played', index=14,
      number=16, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=400,
  serialized_end=853,
)


_HOTBARBUTTONDATA = descriptor.Descriptor(
  name='HotbarButtonData',
  full_name='D3.Hero.HotbarButtonData',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='sno_power', full_name='D3.Hero.HotbarButtonData.sno_power', index=0,
      number=1, type=15, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='gbid_item', full_name='D3.Hero.HotbarButtonData.gbid_item', index=1,
      number=2, type=15, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=855,
  serialized_end=911,
)


_SKILLKEYMAPPING = descriptor.Descriptor(
  name='SkillKeyMapping',
  full_name='D3.Hero.SkillKeyMapping',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='sno_power', full_name='D3.Hero.SkillKeyMapping.sno_power', index=0,
      number=1, type=15, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='id_hotkey', full_name='D3.Hero.SkillKeyMapping.id_hotkey', index=1,
      number=2, type=17, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='skill_button', full_name='D3.Hero.SkillKeyMapping.skill_button', index=2,
      number=3, type=17, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=913,
  serialized_end=990,
)


_SAVEDQUEST = descriptor.Descriptor(
  name='SavedQuest',
  full_name='D3.Hero.SavedQuest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='sno_quest', full_name='D3.Hero.SavedQuest.sno_quest', index=0,
      number=1, type=15, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='difficulty', full_name='D3.Hero.SavedQuest.difficulty', index=1,
      number=2, type=17, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='current_step_uid', full_name='D3.Hero.SavedQuest.current_step_uid', index=2,
      number=3, type=17, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='objective_state', full_name='D3.Hero.SavedQuest.objective_state', index=3,
      number=4, type=17, cpp_type=1, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='failure_condition_state', full_name='D3.Hero.SavedQuest.failure_condition_state', index=4,
      number=5, type=17, cpp_type=1, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=993,
  serialized_end=1128,
)


_LEARNEDLORE = descriptor.Descriptor(
  name='LearnedLore',
  full_name='D3.Hero.LearnedLore',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='sno_lore_learned', full_name='D3.Hero.LearnedLore.sno_lore_learned', index=0,
      number=1, type=15, cpp_type=1, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=1130,
  serialized_end=1169,
)


_SAVEDCONVERSATIONS = descriptor.Descriptor(
  name='SavedConversations',
  full_name='D3.Hero.SavedConversations',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='played_conversations_bitfield', full_name='D3.Hero.SavedConversations.played_conversations_bitfield', index=0,
      number=1, type=12, cpp_type=9, label=2,
      has_default_value=False, default_value="",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='sno_saved_conversations', full_name='D3.Hero.SavedConversations.sno_saved_conversations', index=1,
      number=2, type=15, cpp_type=1, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=1171,
  serialized_end=1263,
)


_SAVEPOINTDATA_PROTO = descriptor.Descriptor(
  name='SavePointData_Proto',
  full_name='D3.Hero.SavePointData_Proto',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='sno_world', full_name='D3.Hero.SavePointData_Proto.sno_world', index=0,
      number=1, type=15, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='savepoint_number', full_name='D3.Hero.SavePointData_Proto.savepoint_number', index=1,
      number=2, type=17, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='creates_portal', full_name='D3.Hero.SavePointData_Proto.creates_portal', index=2,
      number=3, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=1265,
  serialized_end=1355,
)


_SAVEDDATA = descriptor.Descriptor(
  name='SavedData',
  full_name='D3.Hero.SavedData',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='hotbar_button_assignments', full_name='D3.Hero.SavedData.hotbar_button_assignments', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='skill_key_map', full_name='D3.Hero.SavedData.skill_key_map', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='time_played', full_name='D3.Hero.SavedData.time_played', index=2,
      number=3, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='activated_waypoints', full_name='D3.Hero.SavedData.activated_waypoints', index=3,
      number=4, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='hireling_saved_data', full_name='D3.Hero.SavedData.hireling_saved_data', index=4,
      number=5, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='last_level_time', full_name='D3.Hero.SavedData.last_level_time', index=5,
      number=6, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='learned_lore', full_name='D3.Hero.SavedData.learned_lore', index=6,
      number=7, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='saved_conversations', full_name='D3.Hero.SavedData.saved_conversations', index=7,
      number=8, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='sno_active_skills', full_name='D3.Hero.SavedData.sno_active_skills', index=8,
      number=9, type=15, cpp_type=1, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='sno_traits', full_name='D3.Hero.SavedData.sno_traits', index=9,
      number=10, type=15, cpp_type=1, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='seen_tutorials', full_name='D3.Hero.SavedData.seen_tutorials', index=10,
      number=11, type=15, cpp_type=1, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='save_point', full_name='D3.Hero.SavedData.save_point', index=11,
      number=12, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=1358,
  serialized_end=1831,
)


_TIMESTAMPS = descriptor.Descriptor(
  name='Timestamps',
  full_name='D3.Hero.Timestamps',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='create_time', full_name='D3.Hero.Timestamps.create_time', index=0,
      number=1, type=18, cpp_type=2, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='delete_time', full_name='D3.Hero.Timestamps.delete_time', index=1,
      number=2, type=18, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=1833,
  serialized_end=1887,
)


_SAVEDDEFINITION = descriptor.Descriptor(
  name='SavedDefinition',
  full_name='D3.Hero.SavedDefinition',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='version', full_name='D3.Hero.SavedDefinition.version', index=0,
      number=1, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='digest', full_name='D3.Hero.SavedDefinition.digest', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='saved_attributes', full_name='D3.Hero.SavedDefinition.saved_attributes', index=2,
      number=3, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='saved_data', full_name='D3.Hero.SavedDefinition.saved_data', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='saved_quest', full_name='D3.Hero.SavedDefinition.saved_quest', index=4,
      number=5, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='items', full_name='D3.Hero.SavedDefinition.items', index=5,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='quest_reward_history', full_name='D3.Hero.SavedDefinition.quest_reward_history', index=6,
      number=7, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=1890,
  serialized_end=2205,
)


_NAMESEQUENCE = descriptor.Descriptor(
  name='NameSequence',
  full_name='D3.Hero.NameSequence',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='sequence', full_name='D3.Hero.NameSequence.sequence', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=2207,
  serialized_end=2239,
)


_NAMETEXT = descriptor.Descriptor(
  name='NameText',
  full_name='D3.Hero.NameText',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='name', full_name='D3.Hero.NameText.name', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=2241,
  serialized_end=2265,
)


_ESCROW = descriptor.Descriptor(
  name='Escrow',
  full_name='D3.Hero.Escrow',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='version', full_name='D3.Hero.Escrow.version', index=0,
      number=1, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='generator', full_name='D3.Hero.Escrow.generator', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='hero_data', full_name='D3.Hero.Escrow.hero_data', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='state', full_name='D3.Hero.Escrow.state', index=3,
      number=4, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=2267,
  serialized_end=2386,
)

import AttributeSerializer_pb2
import Hireling_pb2
import Items_pb2
import OnlineService_pb2

_VISUALEQUIPMENT.fields_by_name['visual_item'].message_type = _VISUALITEM
_DIGEST.fields_by_name['hero_id'].message_type = OnlineService_pb2._ENTITYID
_DIGEST.fields_by_name['visual_equipment'].message_type = _VISUALEQUIPMENT
_DIGEST.fields_by_name['quest_history'].message_type = _QUESTHISTORYENTRY
_SAVEDDATA.fields_by_name['hotbar_button_assignments'].message_type = _HOTBARBUTTONDATA
_SAVEDDATA.fields_by_name['skill_key_map'].message_type = _SKILLKEYMAPPING
_SAVEDDATA.fields_by_name['hireling_saved_data'].message_type = Hireling_pb2._SAVEDDATA
_SAVEDDATA.fields_by_name['learned_lore'].message_type = _LEARNEDLORE
_SAVEDDATA.fields_by_name['saved_conversations'].message_type = _SAVEDCONVERSATIONS
_SAVEDDATA.fields_by_name['save_point'].message_type = _SAVEPOINTDATA_PROTO
_SAVEDDEFINITION.fields_by_name['digest'].message_type = _DIGEST
_SAVEDDEFINITION.fields_by_name['saved_attributes'].message_type = AttributeSerializer_pb2._SAVEDATTRIBUTES
_SAVEDDEFINITION.fields_by_name['saved_data'].message_type = _SAVEDDATA
_SAVEDDEFINITION.fields_by_name['saved_quest'].message_type = _SAVEDQUEST
_SAVEDDEFINITION.fields_by_name['items'].message_type = Items_pb2._ITEMLIST
_SAVEDDEFINITION.fields_by_name['quest_reward_history'].message_type = _QUESTREWARDHISTORYENTRY
_ESCROW.fields_by_name['generator'].message_type = Items_pb2._GENERATOR
_ESCROW.fields_by_name['hero_data'].message_type = _SAVEDDATA

class VisualItem(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _VISUALITEM
  
  # @@protoc_insertion_point(class_scope:D3.Hero.VisualItem)

class VisualEquipment(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _VISUALEQUIPMENT
  
  # @@protoc_insertion_point(class_scope:D3.Hero.VisualEquipment)

class QuestHistoryEntry(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _QUESTHISTORYENTRY
  
  # @@protoc_insertion_point(class_scope:D3.Hero.QuestHistoryEntry)

class QuestRewardHistoryEntry(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _QUESTREWARDHISTORYENTRY
  
  # @@protoc_insertion_point(class_scope:D3.Hero.QuestRewardHistoryEntry)

class Digest(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _DIGEST
  
  # @@protoc_insertion_point(class_scope:D3.Hero.Digest)

class HotbarButtonData(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _HOTBARBUTTONDATA
  
  # @@protoc_insertion_point(class_scope:D3.Hero.HotbarButtonData)

class SkillKeyMapping(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _SKILLKEYMAPPING
  
  # @@protoc_insertion_point(class_scope:D3.Hero.SkillKeyMapping)

class SavedQuest(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _SAVEDQUEST
  
  # @@protoc_insertion_point(class_scope:D3.Hero.SavedQuest)

class LearnedLore(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _LEARNEDLORE
  
  # @@protoc_insertion_point(class_scope:D3.Hero.LearnedLore)

class SavedConversations(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _SAVEDCONVERSATIONS
  
  # @@protoc_insertion_point(class_scope:D3.Hero.SavedConversations)

class SavePointData_Proto(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _SAVEPOINTDATA_PROTO
  
  # @@protoc_insertion_point(class_scope:D3.Hero.SavePointData_Proto)

class SavedData(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _SAVEDDATA
  
  # @@protoc_insertion_point(class_scope:D3.Hero.SavedData)

class Timestamps(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _TIMESTAMPS
  
  # @@protoc_insertion_point(class_scope:D3.Hero.Timestamps)

class SavedDefinition(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _SAVEDDEFINITION
  
  # @@protoc_insertion_point(class_scope:D3.Hero.SavedDefinition)

class NameSequence(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _NAMESEQUENCE
  
  # @@protoc_insertion_point(class_scope:D3.Hero.NameSequence)

class NameText(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _NAMETEXT
  
  # @@protoc_insertion_point(class_scope:D3.Hero.NameText)

class Escrow(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _ESCROW
  
  # @@protoc_insertion_point(class_scope:D3.Hero.Escrow)

# @@protoc_insertion_point(module_scope)
