from alembic_utils.pg_trigger import PGTrigger
from alembic_utils.pg_function import PGFunction

delete_old = PGFunction(
    schema="public",
    signature="delete_old_schedule()",
    definition="""
    returns trigger as 
    $$ 
    begin
        delete from schedule 
        where end_time < NOW();
        return new;
    end
    $$ language plpgsql
    """,
)

check_old = PGTrigger(
    schema="public",
    signature="check_old_schedule",
    on_entity="schedule",
    definition="""
    after insert or update on schedule
    for each row execute function public.delete_old_schedule();
  """,
)
