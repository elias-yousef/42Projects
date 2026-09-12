/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   push_swap.h                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: mkhashan <mkhashan@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/01/29 11:56:28 by mkhashan          #+#    #+#             */
/*   Updated: 2026/02/06 07:53:36 by mkhashan         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#ifndef PUSH_SWAP_H
# define PUSH_SWAP_H

# include <stdarg.h>
# include <stdio.h>
# include <stdlib.h>
# include <unistd.h>
# include <stdio.h>

typedef struct s_node
{
	int				val;
	struct s_node	*next;
	struct s_node	*prev;
}	t_node;

typedef struct s_stack
{
	int		size;
	t_node	*head;
	int		sx;
	int		ss;
	int		px;
	int		rx;
	int		rr;
	int		rrx;
	int		rrr;
}	t_stack;

typedef struct s_config
{
	int	mod;
	int	bench;
}	t_config;

t_stack	*stack_create(void);
void	clear_stack(t_stack *stack_x);
void	add_node(t_stack *stack, int value);
void	sx(t_stack *stack_x);
void	ss(t_stack *stack_a, t_stack *stack_b);

void	px(t_stack *from, t_stack *to);
void	rx(t_stack *stack_x);
void	rr(t_stack *s1, t_stack *s2);
void	rrx(t_stack *stack_x);
void	rrr(t_stack *s1, t_stack *s2);

long	ft_atoi(char *str);
int		len(char *str);
int		ft_strncmp(char *s1, char *s2, size_t n);
float	compute_disorder(t_stack *stack_a);
int		idx_val(t_stack *stack_a, int idx);
int		d(t_stack *stack_x, int val);
int		is_sorted(t_stack *a);
void	a_1s(void (*f)(t_stack *), t_stack *stack_x, char *ops, int times);
void	a_2s(t_stack *f, t_stack *t, char *ops, int n);

void	start_sort(t_stack *stack_a, t_config *conf);
void	m_sort(t_stack *stack_a, t_stack *stack_b);
void	s_sort(t_stack *a, t_stack *b);
void	c_sort(t_stack *a, t_stack *b);
void	tiny_sort(t_stack *a, t_stack *b);
void	repair_sort(t_stack *a, t_stack *b);
void	bench(t_stack *stack_a, t_stack *stack_b, t_config *conf, float order);

int		ft_printf(const char *format, ...);
int		ft_printnbr(int nbr);
int		ft_printstr(char *str);
int		ft_printfloat(double nbr);

#endif