// Education Hub 2.0 Global TypeScript Definitions

export type UserRole = 'student' | 'university_student' | 'teacher' | 'admin';

export interface Profile {
  id: string;
  email: string;
  full_name: string;
  avatar_url?: string;
  role: UserRole;
  grade_or_course?: string;
  xp_points: number;
  level: number;
  streak_days: number;
  created_at: string;
}

export interface Subject {
  id: string;
  slug: string;
  name: string;
  category: string;
  grade_range: string;
  description: string;
  icon: string;
  color: string;
  total_materials: number;
}

export interface Example {
  title: string;
  problem: string;
  step_by_step: string;
  answer: string;
}

export interface CheckQuestion {
  question: string;
  options: string[];
  correct_index: number;
  explanation: string;
}

export interface Material {
  id: string;
  slug: string;
  subject_id: string;
  subject_name: string;
  title: string;
  grade_level: string;
  difficulty: 'Boshlang'ich' | 'O'rta' | 'Murakkab';
  objective: string;
  theory: string;
  examples: Example[];
  exercise: string;
  exercise_solution: string;
  check_questions: CheckQuestion[];
  tags: string[];
  duration_minutes: number;
  views?: number;
  likes?: number;
}
