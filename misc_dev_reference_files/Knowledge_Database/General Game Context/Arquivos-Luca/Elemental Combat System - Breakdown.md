# **Elemental Combat System: Structure and Flow**

## **1. Overview**:
The combat system is designed for a single-player experience and is turn-based. It emphasizes strategic planning through a Declaration Phase, followed by an Execution Phase. Participants have a set number of Action Points (AP) that dictate how many actions they can take in a round. The system also allows for reactions, letting participants respond to actions taken against them.

## **2. Phases of Combat**:

### **a. Declaration Phase**:
- **GM (Game Master)** presents the combat scenario, including terrain alterations & environmental factors, to the player.
- The player declares their intended actions for the round without spending AP.
- NPCs (Non-Player Characters) also have their actions declared by the GM, either predetermined or based on the situation.

### **b. Initiative Chain**:
- The order of actions is determined based on the nature of declared actions, character stats, or other relevant factors.

### **c. Execution Phase**:
- Actions are executed in the order determined by the Initiative Chain.
- Dice rolls determine the success of actions with variable outcomes.
- AP is spent regardless of the success or failure of an action.
- After each action, opponents can choose to react, spending AP.
- Reactions can be based on the outcome of the dice rolls, the nature of the actions taken, or elemental interactions.

### **d. End of Round**:
- Once all participants have exhausted their AP or choose not to act further, the round ends.
- All participants reset their AP for the next round.
- Damage rolls are made for any successful hits, and effects are applied.

## **3. Action Points (AP)**:
- Each participant has a set number of AP per round.
- Actions have varying AP costs.
- Reactions also cost AP.

## **4. Reactions**:
- Participants can react to actions taken during the Execution Phase.
- The ability to react is determined by the outcome of the dice rolls, the nature of the actions taken, elemental interactions, or other relevant factors.

## **5. Dice Rolls**:
- Dice rolls (typically d20) determine the success, failure, or degree of success for actions.
- Modifiers can be applied based on character stats, elemental advantages, or situational factors.
- The GM informs the player of any advantages or disadvantages before rolls are made.

## **6. GM and Player Interaction**:
- The GM presents the combat scenario and asks the player for their declarations.
- The player declares their chain of actions.
- The GM computes the results of all declared actions, rolls all relevant dice, and initiates the reaction chain.
- The player is informed of actions taken against them and is given the opportunity to react.
- The GM rolls for the outcomes of reactions and informs the player of the results.
- Once all actions and reactions are resolved, the GM concludes the round.

## **7. Terrain Alterations & Environmental Factors**:
- The combat arena can undergo changes due to elemental magic or other factors.
- Terrain features can be used strategically by participants to gain an advantage or hinder opponents.
- Environmental conditions, such as weather, can influence the effectiveness of certain elemental abilities.

## **8. Elemental Interactions**:
- Different elements interact in unique ways, leading to advantages or disadvantages in combat.
- The GM must account for these interactions when elemental magic interacts, influencing the outcome of actions and reactions.

## **9. Skill Progression**:
- Skills progress from single element skills to double and triple element skills.
- Skills consume two resources: mana (related to INT and magic power output) and focus (related to WIS and skill complexity).
- Skills in this elemental system can:
  1. Allow the element to flow through the user.
  2. Manipulate the element present in the environment.
  3. Materialize the element and control it.
  4. Imbue an object with the element, such as a weapon.

## **10. Team Combats & Combo Moves**:
- When accompanied by a friendly NPC, the PC can request the NPC to act in a certain way. The NPC's compliance and the success of the idea depend on the PC's affinity with the NPC and the feasibility of the request.
- The PC can chain actions to form combos, but opponents may react and potentially break the combo.

## **11. Special Abilities**:
- Each character can have a unique special ability that can be used once per combat. This ability can be a game-changer if used strategically.

## **12. Movement & Opportunity Attack System**:
- The traditional movement and opportunity attack systems are replaced by the reaction system.
- There are no specific rules limiting PC movement in combat. However, the GM will determine if a movement action warrants a reaction from one or more opponents.

## **13. Death's Door Mechanic**:
- When the PC's hit points reach 0, they are limited to 1 AP per turn.
- The hit point counter goes negative until -3 hit points.
- Reaching -3 hit points results in the character's permanent death.

## **14. Hit Points Mechanic**:
- Traditional life points and damage roll mechanics are replaced.
- Each successful hit translates to -1 hit point.
- Skills that "do more damage" will deal multiple hits, but each individual hit requires a separate roll.

## **15. Defense Level Mechanic**:
- Defense is calculated based exclusively on character level.
- Defense-enhancing mechanics are contained within skills. For instance, using an ice barrier could raise the defense level by 3 while the barrier is active.

## **16. Influence Points Mechanic**:
- The PC can attempt to influence party members.
- The affinity mechanic is replaced with Influence Points, which reset every turn like AP.
- Influence Points are used to command party members to produce synergizing actions.

# **Sample Character Stat Block - PC**

**Name:** Drakin
**Element:** Shadow
**Weapon:** Katana
**Level:** 3

| Stat  | Value |
|-------|-------|
| STR   | 14    |
| DEX   | 17    |
| CON   | 8     |
| INT   | 15    |
| WIS   | 18    |
| CHA   | 14    |

10 + (LEVEL - 2) = DEFENSE LEVEL = '11'
((DEX - 10)/2) +  2= ACTION POINTS = '5'
INT * 2 = MANA POINTS = '30'
CON = LIFE POINTS = '8'
WIS * 2 = FOCUS POINTS = '36'
(CHA - 10)/2 = INFLUENCE POINTS = '2'
(STR - 10)/2 = BONUS TO WEAPON ATTACK ROLL = '2'

**DEFENSE LEVEL:** 11
**ACTION POINTS:** 5
**MANA POINTS:** 30
**LIFE POINTS:** 8
**FOCUS POINTS:** 36
**INFLUENCE POINTS:** 2
**BONUS TO WEAPON ATTACK ROLL:** 2

---

## **Weapon Skills**

### **1. Swift Slash**
**Skill Type:** Basic Attack
**Description:** A quick horizontal slash aimed at the opponent's torso.
**Effect:** 
- Deals 1 hit point of damage.
- Adds DEX modifier to the attack roll.
**AP Cost:** 1
**Initiative Value:** 2
**Interruptable:** Yes

### **2. Blade Dance**
**Skill Type:** Special Attack
**Description:** A series of rapid slashes, making it hard for the opponent to predict the next move.
**Effect:** 
- Allows two separate attack rolls.
- Each successful hit deals 1 hit point of damage.
**AP Cost:** 3
**Initiative Value:** 3
**Interruptable:** No

### **3. Iaijutsu Strike**
**Skill Type:** Special Attack
**Description:** A lightning-fast draw and slash, catching the opponent off-guard.
**Effect:** 
- Deals 2 hit points of damage.
- If successful by 5 or more, deals an additional hit point of damage.
**AP Cost:** 4
**Initiative Value:** 4
**Interruptable:** No

### **4. Parry**
**Skill Type:** Defensive Maneuver
**Description:** Deflect an incoming attack with the katana.
**Effect:** 
- Grants advantage on the next defensive roll against a melee attack.
**AP Cost:** 1
**Initiative Value:** 1
**Interruptable:** Yes

---

## **Elemental Skills**

### **1. Shadow Strike**
**Skill Type:** Attack
**Description:** A swift katana strike imbued with shadow magic, making it difficult to predict and dodge.
**Effect:** 
- If successful, deals 1 hit point of damage.
- Adds DEX modifier to the attack roll.
**Mana Cost:** 6
**Focus Cost:** 4
**AP Cost:** 2
**Initiative Value:** 3
**Interruptable:** No

### **2. Ephemeral Dodge**
**Skill Type:** Defensive
**Description:** Use the power of shadows to momentarily become intangible, evading physical attacks.
**Effect:** 
- Grants disadvantage to enemy on the next defensive roll against a physical attack.
- Adds WIS modifier to the defensive roll.
**Mana Cost:** 4
**Focus Cost:** 3
**AP Cost:** 1
**Initiative Value:** 2
**Interruptable:** Yes

### **3. Whispering Shadows**
**Skill Type:** Utility
**Description:** Manipulate the shadows around an opponent, confusing and distracting them.
**Effect:** 
- The next skill or attack used by the affected opponent has a disadvantage.
- Adds CHA modifier to the skill roll to determine if the opponent is affected.
**Mana Cost:** 8
**Focus Cost:** 5
**AP Cost:** 2
**Initiative Value:** 1
**Interruptable:** Yes

----



# **Sample Character Stat Block - Friendly NPC**

**Name:** Lunia
**Element:** Water
**Weapon:** Long Bow
**Level:** 3

| Stat  | Value |
|-------|-------|
| STR   | 12    |
| DEX   | 16    |
| CON   | 10    |
| INT   | 18    |
| WIS   | 14    |
| CHA   | 13    |

10 + (LEVEL - 2) = DEFENSE LEVEL = '11'
((DEX - 10)/2) +  2= ACTION POINTS = '5'
INT * 2 = MANA POINTS = '36'
CON = LIFE POINTS = '10'
WIS * 2 = FOCUS POINTS = '28'
(CHA - 10)/2 = INFLUENCE POINTS = '1.5'
(STR - 10)/2 = BONUS TO WEAPON ATTACK ROLL = '1'

**DEFENSE LEVEL:** 11
**ACTION POINTS:** 5
**MANA POINTS:** 36
**LIFE POINTS:** 10
**FOCUS POINTS:** 28
**INFLUENCE POINTS:** 1.5
**BONUS TO WEAPON ATTACK ROLL:** 1

---

## **Weapon Skills**

### **1. Precise Shot**
**Skill Type:** Basic Attack
**Description:** A carefully aimed shot targeting the opponent's vital areas.
**Effect:** 
- Deals 1 hit point of damage.
- Adds DEX modifier to the attack roll.
**AP Cost:** 1
**Initiative Value:** 2
**Interruptable:** Yes

### **2. Rapid Fire**
**Skill Type:** Special Attack
**Description:** Quickly releases multiple arrows in succession.
**Effect:** 
- Allows two separate attack rolls.
- Each successful hit deals 1 hit point of damage.
**AP Cost:** 3
**Initiative Value:** 3
**Interruptable:** No

### **3. Piercing Arrow**
**Skill Type:** Special Attack
**Description:** An arrow shot with great force, capable of penetrating armor.
**Effect:** 
- Deals 2 hit points of damage.
- If successful by 5 or more, deals an additional hit point of damage.
**AP Cost:** 4
**Initiative Value:** 4
**Interruptable:** No

### **4. Evasive Roll**
**Skill Type:** Defensive Maneuver
**Description:** A quick roll to evade incoming attacks.
**Effect:** 
- Grants advantage on the next defensive roll against a ranged attack.
**AP Cost:** 1
**Initiative Value:** 1
**Interruptable:** Yes

---

## **Elemental Skills**

### **1. Water Arrow**
**Skill Type:** Attack
**Description:** Imbues an arrow with water magic, causing it to deal splash damage upon impact.
**Effect:** 
- If successful, deals 1 hit point of damage to the target and 1 hit point of damage to adjacent enemies.
- Adds INT modifier to the attack roll.
**Mana Cost:** 7
**Focus Cost:** 5
**AP Cost:** 2
**Initiative Value:** 3
**Interruptable:** No

### **2. Misty Veil**
**Skill Type:** Defensive
**Description:** Creates a veil of mist around the user, obscuring vision and making them harder to hit.
**Effect:** 
- Grants advantage on the next defensive roll against any attack.
- Adds WIS modifier to the defensive roll.
**Mana Cost:** 5
**Focus Cost:** 4
**AP Cost:** 1
**Initiative Value:** 2
**Interruptable:** Yes

### **3. Tidal Wave**
**Skill Type:** Utility
**Description:** Summons a wave of water to push and disorient opponents.
**Effect:** 
- All enemies in the vicinity are pushed back and have a disadvantage on their next turn.
- Adds CHA modifier to the skill roll to determine the number of affected opponents.
**Mana Cost:** 9
**Focus Cost:** 6
**AP Cost:** 3
**Initiative Value:** 1
**Interruptable:** No

----

# **SAMPLE MONSTER**
## **Poison Wolf (Level 1)**

**Element:** Poison
**Level:** 1

| Stat  | Value |
|-------|-------|
| STR   | 7     |
| DEX   | 8     |
| CON   | 6     |
| INT   | 2     |
| WIS   | 4     |
| CHA   | 3     |

**HIT POINTS:** 4
**ACTION POINTS:** 2

### **Traits/Elements:**
- **Venomous Bite:** The wolf's bite can inject venom, causing additional damage over time.
- **Agile Predator:** The wolf is quick and can dodge attacks with ease.
- **Weak Point:** The wolf's underbelly is less protected, making it vulnerable to attacks targeting this area.

### **Actions:**
#### **1. Bite**
**Skill Type:** Basic Attack
**Description:** The wolf lunges and tries to bite its target.
**Effect:** 
- Deals 1 hit point of damage.
- If successful by 3 or more, the target is poisoned and takes an additional hit point of damage at the start of their next turn.
**AP Cost:** 1
**Initiative Value:** 2
**Interruptable:** Yes

#### **2. Dodge**
**Skill Type:** Defensive
**Description:** The wolf anticipates an attack and attempts to dodge it.
**Effect:** 
- Grants advantage on the next defensive roll against a physical attack.
**AP Cost:** 1
**Initiative Value:** 3
**Interruptable:** Yes

---

## **Earth Boar (Level 2)**

**Element:** Earth
**Level:** 2

| Stat  | Value |
|-------|-------|
| STR   | 10    |
| DEX   | 5     |
| CON   | 9     |
| INT   | 2     |
| WIS   | 3     |
| CHA   | 3     |

**HIT POINTS:** 6
**ACTION POINTS:** 3

### **Traits/Elements:**
- **Sturdy Build:** The boar's body is tough, making it resistant to physical attacks.
- **Charge Attack:** The boar can charge at its enemies, dealing significant damage.
- **Weak Point:** The boar's eyes are sensitive, making it vulnerable to attacks targeting this area.

### **Actions:**
#### **1. Tusk Strike**
**Skill Type:** Basic Attack
**Description:** The boar attempts to gore its target with its tusks.
**Effect:** 
- Deals 2 hit points of damage.
**AP Cost:** 2
**Initiative Value:** 2
**Interruptable:** Yes

#### **2. Charge**
**Skill Type:** Elemental Attack
**Description:** The boar charges at its target, using its momentum to deal damage.
**Effect:** 
- Deals 3 hit points of damage. 
- If successful by 4 or more, knocks the target prone.
**AP Cost:** 3
**Initiative Value:** 1
**Interruptable:** No

---

## **Light Snake (Level 3)**

**Element:** Light
**Level:** 3

| Stat  | Value |
|-------|-------|
| STR   | 4     |
| DEX   | 10    |
| CON   | 5     |
| INT   | 6     |
| WIS   | 7     |
| CHA   | 8     |

**HIT POINTS:** 5
**ACTION POINTS:** 4

### **Traits/Elements:**
- **Luminous Scales:** The snake's scales emit a bright light, which can be blinding to its enemies.
- **Quick Reflexes:** The snake can react quickly to incoming threats.
- **Weak Point:** The snake's head is its most vulnerable point.

### **Actions:**
#### **1. Bite**
**Skill Type:** Basic Attack
**Description:** The snake lunges and tries to bite its target.
**Effect:** 
- Deals 1 hit point of damage.
**AP Cost:** 1
**Initiative Value:** 3
**Interruptable:** Yes

#### **2. Constrict**
**Skill Type:** Basic Attack
**Description:** The snake attempts to wrap around its target, squeezing and binding them.
**Effect:** 
- The target is restrained and takes 1 hit point of damage at the start of their next turn.
**AP Cost:** 2
**Initiative Value:** 2
**Interruptable:** Yes

#### **3. Blinding Flash**
**Skill Type:** Elemental Attack
**Description:** The snake's scales emit a blinding light.
**Effect:** 
- All enemies in the vicinity are blinded for their next turn.
**AP Cost:** 3
**Initiative Value:** 1 
**Interruptable:** No



# RELEVANT ELEMENTAL INTERACTIONS

1. Drakin (Shadow) can nullify any light-based attacks or effects from the Light Snake.
2. The Light Snake (Light) can nullify any shadow-based attacks or effects from Drakin.
3. Lunia (Water) can combine her water-based attacks with the Earth Boar's earth-based attacks to create mud or swamp effects.