import { createClient } from '@supabase/supabase-js'

const supabaseUrl = import.meta.env.SVELTE_APP_SUPABASE_URL
const supabaseAnonKey = import.meta.env.SVELTE_APP_SUPABASE_ANON_KEY

export const supabase = createClient(supabaseUrl, supabaseAnonKey)