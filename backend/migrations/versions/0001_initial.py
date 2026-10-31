"""Create identity, farms and soil tables."""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql
revision='0001_initial'
down_revision=None
branch_labels=None
depends_on=None
def upgrade():
 uuid_type=sa.Uuid()
 op.create_table('users',sa.Column('id',uuid_type,primary_key=True),sa.Column('full_name',sa.String(120),nullable=False),sa.Column('phone_e164',sa.String(20),nullable=False),sa.Column('email',sa.String(255)),sa.Column('password_hash',sa.String(255),nullable=False),sa.Column('preferred_language',sa.String(8),nullable=False,server_default='bn'),sa.Column('account_status',sa.String(20),nullable=False,server_default='active'),sa.Column('created_at',sa.DateTime(timezone=True),server_default=sa.func.now(),nullable=False),sa.UniqueConstraint('phone_e164'),sa.UniqueConstraint('email'))
 op.create_index('ix_users_phone_e164','users',['phone_e164'])
 op.create_table('farms',sa.Column('id',uuid_type,primary_key=True),sa.Column('owner_user_id',uuid_type,sa.ForeignKey('users.id',ondelete='CASCADE'),nullable=False),sa.Column('name',sa.String(120),nullable=False),sa.Column('district',sa.String(100),nullable=False),sa.Column('block',sa.String(100)),sa.Column('village',sa.String(100)),sa.Column('address_text',sa.Text()),sa.Column('total_area',sa.Numeric(12,3),nullable=False),sa.Column('area_unit',sa.String(20),nullable=False),sa.Column('soil_texture',sa.String(50)),sa.Column('irrigation_type',sa.String(50)),sa.Column('verification_status',sa.String(24),nullable=False,server_default='unverified'),sa.Column('created_at',sa.DateTime(timezone=True),server_default=sa.func.now(),nullable=False),sa.Column('updated_at',sa.DateTime(timezone=True),server_default=sa.func.now(),nullable=False))
 op.create_index('ix_farms_owner_user_id','farms',['owner_user_id'])
 op.create_table('soil_samples',sa.Column('id',uuid_type,primary_key=True),sa.Column('farm_id',uuid_type,sa.ForeignKey('farms.id',ondelete='CASCADE'),nullable=False),sa.Column('collected_at',sa.DateTime(timezone=True),nullable=False),sa.Column('source_type',sa.String(20),nullable=False,server_default='manual'),sa.Column('lab_name',sa.String(160)),sa.Column('notes',sa.Text()),sa.Column('created_at',sa.DateTime(timezone=True),server_default=sa.func.now(),nullable=False))
 op.create_index('ix_soil_samples_farm_id','soil_samples',['farm_id'])
 op.create_table('soil_test_results',sa.Column('id',uuid_type,primary_key=True),sa.Column('soil_sample_id',uuid_type,sa.ForeignKey('soil_samples.id',ondelete='CASCADE'),nullable=False),sa.Column('parameter_code',sa.String(40),nullable=False),sa.Column('numeric_value',sa.Numeric(14,5),nullable=False),sa.Column('unit',sa.String(40),nullable=False),sa.Column('method',sa.String(120)),sa.UniqueConstraint('soil_sample_id','parameter_code',name='uq_soil_sample_parameter'))
 op.create_index('ix_soil_test_results_soil_sample_id','soil_test_results',['soil_sample_id'])
def downgrade():
 op.drop_index('ix_soil_test_results_soil_sample_id',table_name='soil_test_results'); op.drop_table('soil_test_results')
 op.drop_index('ix_soil_samples_farm_id',table_name='soil_samples'); op.drop_table('soil_samples')
 op.drop_index('ix_farms_owner_user_id',table_name='farms'); op.drop_table('farms')
 op.drop_index('ix_users_phone_e164',table_name='users'); op.drop_table('users')
