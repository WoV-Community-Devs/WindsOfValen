export const Shields = [
  // ── Block Shields ──
  {
    Name: "Skeleton Shield",
    Description: "Weak defensive shield, can mitigate heavy attacks.",
    Icon: "skeleton_shield",
    Type: "SHIELD",
    Requirements: [{ Skill: "DEFENSE", Value: 1 }],
    Stats: [{ Type: "BLOCK_POWER", Value: 25 }],
  },
  {
    Name: "Iron Shield",
    Description: "Basic defensive shield, can mitigate heavy attacks.",
    Icon: "iron_shield",
    Type: "SHIELD",
    Requirements: [{ Skill: "DEFENSE", Value: 10 }],
    Stats: [{ Type: "BLOCK_POWER", Value: 35 }],
  },
  {
    Name: "Steel Shield",
    Description: "Useful defensive shield, can mitigate heavy attacks.",
    Icon: "steel_shield",
    Type: "SHIELD",
    Requirements: [{ Skill: "DEFENSE", Value: 20 }],
    Stats: [{ Type: "BLOCK_POWER", Value: 50 }],
  },
  {
    Name: "Elven Shield",
    Description: "Powerful defensive shield, can mitigate heavy attacks.",
    Icon: "elven_shield",
    Type: "SHIELD",
    Requirements: [{ Skill: "DEFENSE", Value: 30 }],
    Stats: [{ Type: "BLOCK_POWER", Value: 70 }],
  },
  // ── Parry Shields (Deflect) ──
  {
    Name: "Parry Shield",
    Description: "Useful evasion shield, can mitigate quick attacks.",
    Icon: "parry_shield",
    Type: "SHIELD",
    Requirements: [{ Skill: "EVASION", Value: 1 }],
    Stats: [{ Type: "DEFLECT_POWER", Value: 50 }],
  },
  {
    Name: "Advanced Parry Shield",
    Description: "Powerful evasion shield, can mitigate quick attacks.",
    Icon: "advanced_parry_shield",
    Type: "SHIELD",
    Requirements: [{ Skill: "EVASION", Value: 20 }],
    Stats: [{ Type: "DEFLECT_POWER", Value: 70 }],
  },
  // ── Wards ──
  {
    Name: "Novice Ward",
    Type: "SHIELD",
    Requirements: [{ Skill: "WARDING", Value: 1 }],
    Stats: [{ Type: "WARD_POWER", Value: 35 }],
  },
  {
    Name: "Apprentice Ward",
    Type: "SHIELD",
    Requirements: [{ Skill: "WARDING", Value: 10 }],
    Stats: [{ Type: "WARD_POWER", Value: 50 }],
  },
  {
    Name: "Adept Ward",
    Type: "SHIELD",
    Requirements: [{ Skill: "WARDING", Value: 20 }],
    Stats: [{ Type: "DEFLECT_POWER", Value: 70 }],
  },
];
