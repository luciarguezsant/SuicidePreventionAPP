��
��
D
AddV2
x"T
y"T
z"T"
Ttype:
2	��
h
Any	
input

reduction_indices"Tidx

output
"
	keep_dimsbool( "
Tidxtype0:
2	
^
AssignVariableOp
resource
value"dtype"
dtypetype"
validate_shapebool( �
N
Cast	
x"SrcT	
y"DstT"
SrcTtype"
DstTtype"
Truncatebool( 
8
Const
output"dtype"
valuetensor"
dtypetype
=
Greater
x"T
y"T
z
"
Ttype:
2	
.
Identity

input"T
output"T"	
Ttype
+
IsNan
x"T
y
"
Ttype:
2
q
MatMul
a"T
b"T
product"T"
transpose_abool( "
transpose_bbool( "
Ttype:

2	
�
MergeV2Checkpoints
checkpoint_prefixes
destination_prefix"
delete_old_dirsbool("
allow_missing_filesbool( �

NoOp
M
Pack
values"T*N
output"T"
Nint(0"	
Ttype"
axisint 
C
Placeholder
output"dtype"
dtypetype"
shapeshape:
@
ReadVariableOp
resource
value"dtype"
dtypetype�
@
RealDiv
x"T
y"T
z"T"
Ttype:
2	
o
	RestoreV2

prefix
tensor_names
shape_and_slices
tensors2dtypes"
dtypes
list(type)(0�
l
SaveV2

prefix
tensor_names
shape_and_slices
tensors2dtypes"
dtypes
list(type)(0�
?
Select
	condition

t"T
e"T
output"T"	
Ttype
H
ShardedFilename
basename	
shard

num_shards
filename
0
Sigmoid
x"T
y"T"
Ttype:

2
N
Squeeze

input"T
output"T"	
Ttype"
squeeze_dims	list(int)
 (
�
StatefulPartitionedCall
args2Tin
output2Tout"
Tin
list(type)("
Tout
list(type)("	
ffunc"
configstring "
config_protostring "
executor_typestring ��
�
StatelessIf
cond"Tcond
input2Tin
output2Tout"
Tcondtype"
Tin
list(type)("
Tout
list(type)("
then_branchfunc"
else_branchfunc" 
output_shapeslist(shape)
 
@
StaticRegexFullMatch	
input

output
"
patternstring
N

StringJoin
inputs*N

output"
Nint(0"
	separatorstring 
<
Sub
x"T
y"T
z"T"
Ttype:
2	
�
VarHandleOp
resource"
	containerstring "
shared_namestring "
dtypetype"
shapeshape"#
allowed_deviceslist(string)
 �"serve*2.11.02v2.11.0-rc2-15-g6290819256d8�l
i
VariableVarHandleOp*
_output_shapes
: *
dtype0*
shape:�*
shared_name
Variable
b
Variable/Read/ReadVariableOpReadVariableOpVariable*
_output_shapes	
:�*
dtype0
m

Variable_1VarHandleOp*
_output_shapes
: *
dtype0*
shape:�*
shared_name
Variable_1
f
Variable_1/Read/ReadVariableOpReadVariableOp
Variable_1*
_output_shapes	
:�*
dtype0
h

Variable_2VarHandleOp*
_output_shapes
: *
dtype0*
shape: *
shared_name
Variable_2
a
Variable_2/Read/ReadVariableOpReadVariableOp
Variable_2*
_output_shapes
: *
dtype0
q

Variable_3VarHandleOp*
_output_shapes
: *
dtype0*
shape:	�*
shared_name
Variable_3
j
Variable_3/Read/ReadVariableOpReadVariableOp
Variable_3*
_output_shapes
:	�*
dtype0
�
serving_default_xPlaceholder*0
_output_shapes
:������������������*
dtype0*%
shape:������������������
�
StatefulPartitionedCallStatefulPartitionedCallserving_default_x
Variable_1Variable
Variable_3
Variable_2*
Tin	
2*
Tout
2*
_collective_manager_ids
 *#
_output_shapes
:���������*&
_read_only_resource_inputs
*-
config_proto

CPU

GPU 2J 8� */
f*R(
&__inference_signature_wrapper_26286770

NoOpNoOp
�
ConstConst"/device:CPU:0*
_output_shapes
: *
dtype0*�
value�B� B�
@
	model

norm_x
get_predictions

signatures*

w
b*

mean
std*

	trace_0* 


serving_default* 
F@
VARIABLE_VALUE
Variable_3"model/w/.ATTRIBUTES/VARIABLE_VALUE*
F@
VARIABLE_VALUE
Variable_2"model/b/.ATTRIBUTES/VARIABLE_VALUE*
JD
VARIABLE_VALUE
Variable_1&norm_x/mean/.ATTRIBUTES/VARIABLE_VALUE*
GA
VARIABLE_VALUEVariable%norm_x/std/.ATTRIBUTES/VARIABLE_VALUE*
* 
* 
O
saver_filenamePlaceholder*
_output_shapes
: *
dtype0*
shape: 
�
StatefulPartitionedCall_1StatefulPartitionedCallsaver_filenameVariable_3/Read/ReadVariableOpVariable_2/Read/ReadVariableOpVariable_1/Read/ReadVariableOpVariable/Read/ReadVariableOpConst*
Tin

2*
Tout
2*
_collective_manager_ids
 *
_output_shapes
: * 
_read_only_resource_inputs
 *-
config_proto

CPU

GPU 2J 8� **
f%R#
!__inference__traced_save_26286805
�
StatefulPartitionedCall_2StatefulPartitionedCallsaver_filename
Variable_3
Variable_2
Variable_1Variable*
Tin	
2*
Tout
2*
_collective_manager_ids
 *
_output_shapes
: * 
_read_only_resource_inputs
 *-
config_proto

CPU

GPU 2J 8� *-
f(R&
$__inference__traced_restore_26286827�W
�
(
cond_false_26286728
cond_identityL

cond/ConstConst*
_output_shapes
: *
dtype0*
value	B : N
cond/Const_1Const*
_output_shapes
: *
dtype0*
value	B : N
cond/Const_2Const*
_output_shapes
: *
dtype0*
value	B : Q
cond/IdentityIdentitycond/Const_2:output:0*
T0*
_output_shapes
: "'
cond_identitycond/Identity:output:0*(
_construction_contextkEagerRuntime*
_input_shapes 
�
�
$__inference__traced_restore_26286827
file_prefix.
assignvariableop_variable_3:	�'
assignvariableop_1_variable_2: ,
assignvariableop_2_variable_1:	�*
assignvariableop_3_variable:	�

identity_5��AssignVariableOp�AssignVariableOp_1�AssignVariableOp_2�AssignVariableOp_3�
RestoreV2/tensor_namesConst"/device:CPU:0*
_output_shapes
:*
dtype0*�
value�B�B"model/w/.ATTRIBUTES/VARIABLE_VALUEB"model/b/.ATTRIBUTES/VARIABLE_VALUEB&norm_x/mean/.ATTRIBUTES/VARIABLE_VALUEB%norm_x/std/.ATTRIBUTES/VARIABLE_VALUEB_CHECKPOINTABLE_OBJECT_GRAPHz
RestoreV2/shape_and_slicesConst"/device:CPU:0*
_output_shapes
:*
dtype0*
valueBB B B B B �
	RestoreV2	RestoreV2file_prefixRestoreV2/tensor_names:output:0#RestoreV2/shape_and_slices:output:0"/device:CPU:0*(
_output_shapes
:::::*
dtypes	
2[
IdentityIdentityRestoreV2:tensors:0"/device:CPU:0*
T0*
_output_shapes
:�
AssignVariableOpAssignVariableOpassignvariableop_variable_3Identity:output:0"/device:CPU:0*&
 _has_manual_control_dependencies(*
_output_shapes
 *
dtype0]

Identity_1IdentityRestoreV2:tensors:1"/device:CPU:0*
T0*
_output_shapes
:�
AssignVariableOp_1AssignVariableOpassignvariableop_1_variable_2Identity_1:output:0"/device:CPU:0*&
 _has_manual_control_dependencies(*
_output_shapes
 *
dtype0]

Identity_2IdentityRestoreV2:tensors:2"/device:CPU:0*
T0*
_output_shapes
:�
AssignVariableOp_2AssignVariableOpassignvariableop_2_variable_1Identity_2:output:0"/device:CPU:0*&
 _has_manual_control_dependencies(*
_output_shapes
 *
dtype0]

Identity_3IdentityRestoreV2:tensors:3"/device:CPU:0*
T0*
_output_shapes
:�
AssignVariableOp_3AssignVariableOpassignvariableop_3_variableIdentity_3:output:0"/device:CPU:0*&
 _has_manual_control_dependencies(*
_output_shapes
 *
dtype0Y
NoOpNoOp"/device:CPU:0*&
 _has_manual_control_dependencies(*
_output_shapes
 �

Identity_4Identityfile_prefix^AssignVariableOp^AssignVariableOp_1^AssignVariableOp_2^AssignVariableOp_3^NoOp"/device:CPU:0*
T0*
_output_shapes
: U

Identity_5IdentityIdentity_4:output:0^NoOp_1*
T0*
_output_shapes
: �
NoOp_1NoOp^AssignVariableOp^AssignVariableOp_1^AssignVariableOp_2^AssignVariableOp_3*"
_acd_function_control_output(*
_output_shapes
 "!

identity_5Identity_5:output:0*
_input_shapes

: : : : : 2$
AssignVariableOpAssignVariableOp2(
AssignVariableOp_1AssignVariableOp_12(
AssignVariableOp_2AssignVariableOp_22(
AssignVariableOp_3AssignVariableOp_3:C ?

_output_shapes
: 
%
_user_specified_namefile_prefix
�
�
&__inference_signature_wrapper_26286770
x
unknown:	�
	unknown_0:	�
	unknown_1:	�
	unknown_2: 
identity��StatefulPartitionedCall�
StatefulPartitionedCallStatefulPartitionedCallxunknown	unknown_0	unknown_1	unknown_2*
Tin	
2*
Tout
2*
_collective_manager_ids
 *#
_output_shapes
:���������*&
_read_only_resource_inputs
*-
config_proto

CPU

GPU 2J 8� *-
f(R&
$__inference_get_predictions_26286755k
IdentityIdentity StatefulPartitionedCall:output:0^NoOp*
T0*#
_output_shapes
:���������`
NoOpNoOp^StatefulPartitionedCall*"
_acd_function_control_output(*
_output_shapes
 "
identityIdentity:output:0*(
_construction_contextkEagerRuntime*7
_input_shapes&
$:������������������: : : : 22
StatefulPartitionedCallStatefulPartitionedCall:S O
0
_output_shapes
:������������������

_user_specified_namex
�
�
!__inference__traced_save_26286805
file_prefix)
%savev2_variable_3_read_readvariableop)
%savev2_variable_2_read_readvariableop)
%savev2_variable_1_read_readvariableop'
#savev2_variable_read_readvariableop
savev2_const

identity_1��MergeV2Checkpointsw
StaticRegexFullMatchStaticRegexFullMatchfile_prefix"/device:CPU:**
_output_shapes
: *
pattern
^s3://.*Z
ConstConst"/device:CPU:**
_output_shapes
: *
dtype0*
valueB B.parta
Const_1Const"/device:CPU:**
_output_shapes
: *
dtype0*
valueB B
_temp/part�
SelectSelectStaticRegexFullMatch:output:0Const:output:0Const_1:output:0"/device:CPU:**
T0*
_output_shapes
: f

StringJoin
StringJoinfile_prefixSelect:output:0"/device:CPU:**
N*
_output_shapes
: L

num_shardsConst*
_output_shapes
: *
dtype0*
value	B :f
ShardedFilename/shardConst"/device:CPU:0*
_output_shapes
: *
dtype0*
value	B : �
ShardedFilenameShardedFilenameStringJoin:output:0ShardedFilename/shard:output:0num_shards:output:0"/device:CPU:0*
_output_shapes
: �
SaveV2/tensor_namesConst"/device:CPU:0*
_output_shapes
:*
dtype0*�
value�B�B"model/w/.ATTRIBUTES/VARIABLE_VALUEB"model/b/.ATTRIBUTES/VARIABLE_VALUEB&norm_x/mean/.ATTRIBUTES/VARIABLE_VALUEB%norm_x/std/.ATTRIBUTES/VARIABLE_VALUEB_CHECKPOINTABLE_OBJECT_GRAPHw
SaveV2/shape_and_slicesConst"/device:CPU:0*
_output_shapes
:*
dtype0*
valueBB B B B B �
SaveV2SaveV2ShardedFilename:filename:0SaveV2/tensor_names:output:0 SaveV2/shape_and_slices:output:0%savev2_variable_3_read_readvariableop%savev2_variable_2_read_readvariableop%savev2_variable_1_read_readvariableop#savev2_variable_read_readvariableopsavev2_const"/device:CPU:0*&
 _has_manual_control_dependencies(*
_output_shapes
 *
dtypes	
2�
&MergeV2Checkpoints/checkpoint_prefixesPackShardedFilename:filename:0^SaveV2"/device:CPU:0*
N*
T0*
_output_shapes
:�
MergeV2CheckpointsMergeV2Checkpoints/MergeV2Checkpoints/checkpoint_prefixes:output:0file_prefix"/device:CPU:0*&
 _has_manual_control_dependencies(*
_output_shapes
 f
IdentityIdentityfile_prefix^MergeV2Checkpoints"/device:CPU:0*
T0*
_output_shapes
: Q

Identity_1IdentityIdentity:output:0^NoOp*
T0*
_output_shapes
: [
NoOpNoOp^MergeV2Checkpoints*"
_acd_function_control_output(*
_output_shapes
 "!

identity_1Identity_1:output:0*2
_input_shapes!
: :	�: :�:�: 2(
MergeV2CheckpointsMergeV2Checkpoints:C ?

_output_shapes
: 
%
_user_specified_namefile_prefix:%!

_output_shapes
:	�:

_output_shapes
: :!

_output_shapes	
:�:!

_output_shapes	
:�:

_output_shapes
: 
�
�
$__inference_get_predictions_26286755
x*
sub_readvariableop_resource:	�.
truediv_readvariableop_resource:	�1
matmul_readvariableop_resource:	�%
add_readvariableop_resource: 
identity��Add/ReadVariableOp�MatMul/ReadVariableOp�sub/ReadVariableOp�sub_1/ReadVariableOp�truediv/ReadVariableOp�truediv_1/ReadVariableOpk
sub/ReadVariableOpReadVariableOpsub_readvariableop_resource*
_output_shapes	
:�*
dtype0`
sub/subSubxsub/ReadVariableOp:value:0*
T0*(
_output_shapes
:����������s
truediv/ReadVariableOpReadVariableOptruediv_readvariableop_resource*
_output_shapes	
:�*
dtype0z
truediv/truedivRealDivsub/sub:z:0truediv/ReadVariableOp:value:0*
T0*(
_output_shapes
:����������V
IsNanIsNantruediv/truediv:z:0*
T0*(
_output_shapes
:����������V
ConstConst*
_output_shapes
:*
dtype0*
valueB"       =
AnyAny	IsNan:y:0Const:output:0*
_output_shapes
: �
condStatelessIfAny:output:0*
Tcond0
*	
Tin
 *
Tout
2*
_lower_using_switch_merge(*
_output_shapes
: * 
_read_only_resource_inputs
 *&
else_branchR
cond_false_26286728*
output_shapes
: *%
then_branchR
cond_true_26286727I
cond/IdentityIdentitycond:output:0*
T0*
_output_shapes
: m
sub_1/ReadVariableOpReadVariableOpsub_readvariableop_resource*
_output_shapes	
:�*
dtype0d
	sub_1/subSubxsub_1/ReadVariableOp:value:0*
T0*(
_output_shapes
:����������u
truediv_1/ReadVariableOpReadVariableOptruediv_readvariableop_resource*
_output_shapes	
:�*
dtype0�
truediv_1/truedivRealDivsub_1/sub:z:0 truediv_1/ReadVariableOp:value:0*
T0*(
_output_shapes
:����������u
MatMul/ReadVariableOpReadVariableOpmatmul_readvariableop_resource*
_output_shapes
:	�*
dtype0x
MatMulMatMultruediv_1/truediv:z:0MatMul/ReadVariableOp:value:0*
T0*'
_output_shapes
:���������f
Add/ReadVariableOpReadVariableOpadd_readvariableop_resource*
_output_shapes
: *
dtype0l
AddAddV2MatMul:product:0Add/ReadVariableOp:value:0*
T0*'
_output_shapes
:���������`
SqueezeSqueezeAdd:z:0*
T0*#
_output_shapes
:���������*
squeeze_dims
R
SigmoidSigmoidSqueeze:output:0*
T0*#
_output_shapes
:���������L
Const_1Const*
_output_shapes
: *
dtype0*
valueB
 *   ?_
GreaterGreaterSigmoid:y:0Const_1:output:0*
T0*#
_output_shapes
:���������V
CastCastGreater:z:0*

DstT0*

SrcT0
*#
_output_shapes
:���������S
IdentityIdentityCast:y:0^NoOp*
T0*#
_output_shapes
:����������
NoOpNoOp^Add/ReadVariableOp^MatMul/ReadVariableOp^sub/ReadVariableOp^sub_1/ReadVariableOp^truediv/ReadVariableOp^truediv_1/ReadVariableOp*"
_acd_function_control_output(*
_output_shapes
 "
identityIdentity:output:0*(
_construction_contextkEagerRuntime*7
_input_shapes&
$:������������������: : : : 2(
Add/ReadVariableOpAdd/ReadVariableOp2.
MatMul/ReadVariableOpMatMul/ReadVariableOp2(
sub/ReadVariableOpsub/ReadVariableOp2,
sub_1/ReadVariableOpsub_1/ReadVariableOp20
truediv/ReadVariableOptruediv/ReadVariableOp24
truediv_1/ReadVariableOptruediv_1/ReadVariableOp:S O
0
_output_shapes
:������������������

_user_specified_namex
�
'
cond_true_26286727
cond_identityL

cond/ConstConst*
_output_shapes
: *
dtype0*
value	B : O
cond/IdentityIdentitycond/Const:output:0*
T0*
_output_shapes
: "'
cond_identitycond/Identity:output:0*(
_construction_contextkEagerRuntime*
_input_shapes "�
L
saver_filename:0StatefulPartitionedCall_1:0StatefulPartitionedCall_28"
saved_model_main_op

NoOp*>
__saved_model_init_op%#
__saved_model_init_op

NoOp*�
serving_default�
8
x3
serving_default_x:0������������������8
output_0,
StatefulPartitionedCall:0���������tensorflow/serving/predict:�

Z
	model

norm_x
get_predictions

signatures"
_generic_user_object
,
w
b"
_generic_user_object
1
mean
std"
_generic_user_object
�
	trace_02�
$__inference_get_predictions_26286755�
���
FullArgSpec
args�
jself
jx
varargs
 
varkw
 
defaults
 

kwonlyargs� 
kwonlydefaults
 
annotations� *&�#
!�������������������z	trace_0
,

serving_default"
signature_map
:	�2Variable
: 2Variable
:�2Variable
:�2Variable
�B�
$__inference_get_predictions_26286755x"�
���
FullArgSpec
args�
jself
jx
varargs
 
varkw
 
defaults
 

kwonlyargs� 
kwonlydefaults
 
annotations� *&�#
!�������������������
�B�
&__inference_signature_wrapper_26286770x"�
���
FullArgSpec
args� 
varargs
 
varkwjkwargs
defaults
 

kwonlyargs� 
kwonlydefaults
 
annotations� *
 �
$__inference_get_predictions_26286755Z3�0
)�&
$�!
x������������������
� "�
unknown����������
&__inference_signature_wrapper_26286770q8�5
� 
.�+
)
x$�!
x������������������"/�,
*
output_0�
output_0���������